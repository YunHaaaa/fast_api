from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()

class DataInput(BaseModel):
    name: str


@app.get("/")
def home():
    return {"Hello" : "GET"}


@app.post("/")
def home_post(data_request:DataInput):
    return {"Hello" : "POST", "msg" : data_request.name}