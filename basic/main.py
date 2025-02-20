from typing import Union
from fastapi import FastAPI

import model
model = model.AndModel()  # model.py 를 임포트하고 AndModel 클래스의 인스턴스 생성

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# /items/{item_id} 경로
# 주소를 기반으로 요청
# {item_id} 경로 파라미터
@app.get("/items/{item_id}")  # endpoint
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/predict/left/{left}/right/{right}")  # left, right를 받아옴 (input_data 형식이 [0,0]부터 [1,1]이기 때문)
def predict(left:int, right:int):
    result = model.predict([left, right])
    return {"result": result}


@app.post("/train")
def train():
    model.train()
    return {"result": "OK"}