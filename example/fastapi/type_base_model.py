from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] # int, float 둘 다 가능
    tag: Optional[str] # str이고 기본 값은 none
    date: Optional[datetime]
    some_variable_list: List[int] = [] # int로 구성된 리스트, 기본값은 []

class User(BaseModel):
    '''
    gt : 설정된 값보다 큰
    ge : 설정된 값보다 크거나 작은
    lt : 설정된 값보다 작은
    le : 설정된 값보다 작거나 같은
    '''
    uid: int
    name: str = Field(min_length=2, max_length=7)
    age: int = Field(gt=1, le=130)


tmp_movie_data = {
    'mid' : '1',
    'genre' : 'action',
    'rate' : 1.5,
    'tag' : None,
    'date' : '2023-01-03 19:12:11'
}

tmp_user_data = {
    'uid' : '100',
    'name' : 'soojin',
    'age' : '12'
}

tmp_movie = Movie(**tmp_movie_data)
tmp_user = User(**tmp_user_data)
print(tmp_movie.model_dump_json())
print(tmp_user.model_dump_json())