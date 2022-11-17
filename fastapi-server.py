import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_root(x: int, y: int):
    return x + y


uvicorn.run(app, host='0.0.0.0', port=8888, log_level='critical')
