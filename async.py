import asyncio
# import time
from fastapi import FastAPI


async def some_library(num:int, something:str):
    s = 0
    for i in range(num):
        print("something : ", something, i)
        # time.sleep : 동기적으로 작동하는 함수
        # asyncio.sleep : 비동기적으로 작동하는 함수
        await asyncio.sleep(1)
        s += int(something)
    return s


app = FastAPI()


@app.post("/")
async def read_results(something:str):
    s1 = await some_library(5, something)
    return {"data" : "data", "s1" : s1}

