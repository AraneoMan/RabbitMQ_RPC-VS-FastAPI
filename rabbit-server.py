from time import sleep

import pika


sleep(10)  # wait RabbitMQ

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbit', port=5672)
)

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def sumer(x: int, y: int) -> int:
    return x + y


def on_request(ch, method, props, body: bytes):
    x, y = body.decode('utf-8').split(',')
    response = str(sumer(int(x), int(y)))

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=response.encode('utf-8')
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

channel.start_consuming()
