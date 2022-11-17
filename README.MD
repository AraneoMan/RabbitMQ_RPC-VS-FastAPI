### Check symple FastAPI speed:
```commandline
docker-compose -f compose-fast.yml up --build
```
Output:
```commandline
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 1.0906437873840331 seconds
src-test_server-1  | Errors 0.0%
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 1.0874282598495484 seconds
src-test_server-1  | Errors 0.0%
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 1.0720941305160523 seconds
src-test_server-1  | Errors 0.0%
```

### Check symple RabbitMQ RPC speed:
```commandline
docker-compose -f compose-rabbit.yml up --build
```
Output:
```commandline
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 0.5769391298294068 seconds
src-test_server-1  | Errors 0.0%
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 0.5573016166687011 seconds
src-test_server-1  | Errors 0.0%
src-test_server-1  | Testing...
src-test_server-1  | Process 1000 calls in 0.5703194618225098 seconds
src-test_server-1  | Errors 0.0%
```