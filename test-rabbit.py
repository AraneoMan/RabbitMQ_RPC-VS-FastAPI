from time import time, sleep

import pika


sleep(10)  # wait RabbitMQ

COUNT_TESTS = 10
COUNT_CALLS_BY_TEST = 1000


class ClientRPC(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit', port=5672)
        )

        self.channel = self.connection.channel()

        res = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = res.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response: int = 0

    def on_response(self, ch, method, props, body: bytes):
        self.response = int(body.decode('utf-8'))

    def call(self, x: int, y: int):
        self.response = 0
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
            ),
            body=f'{x},{y}'.encode('utf-8'))
        self.connection.process_data_events(time_limit=None)
        return int(self.response)


client = ClientRPC()

while True:
    result = 99_999_999
    right = 0
    fail = 0
    timer = 0

    print('Testing...')

    for _ in range(COUNT_TESTS):
        start_time = time()
        for i in range(COUNT_CALLS_BY_TEST):
            response = client.call(12345678, 87654321+i)
            if response == result + i:
                right += 1
            else:
                fail += 1
        timer += time() - start_time

    print(f'Process {COUNT_CALLS_BY_TEST} calls in {timer / COUNT_TESTS} seconds')
    print(f'Errors {(fail/right)*100}%')
