from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]


@app.get("/")
# async def root():
def root():
    return {"message" : "Hello World"}


@app.get("/home")
def home():
    return {"message" : "home"}


@app.get("/home/{name}")
def read_name(name:str):
    return {'name' : name}


@app.get("/home_err/{name}")
def read_name_err(name:int):
    return {'name' : name}


@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message" : "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name" : model_name, "message" : "LeCNN all the images"}
    
    return {"model_name" : model_name, "message" : "Have some residuals"}


@app.get("/items/{item_id}")
def read_item(item_id:str, skip:int=0, limit:int=10):
    return fake_items_db[skip : skip + limit]
