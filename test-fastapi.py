from time import time, sleep
from urllib import request


COUNT_TESTS = 10
COUNT_CALLS_BY_TEST = 1000
URL = 'http://server:8888?x={}&y={}'

while True:
    result = 99_999_999
    right = 0
    fail = 0
    timer = 0

    print('Testing...')

    for _ in range(COUNT_TESTS):
        start_time = time()
        for i in range(COUNT_CALLS_BY_TEST):
            response = request.urlopen(URL.format(12345678, 87654321+i)).read()
            response = int(response.decode('utf-8'))
            if response == result + i:
                right += 1
            else:
                fail += 1
        timer += time() - start_time

    print(f'Process {COUNT_CALLS_BY_TEST} calls in {timer / COUNT_TESTS} seconds')
    print(f'Errors {(fail/right)*100}%')

