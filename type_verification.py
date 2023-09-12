from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] # int, float 둘 다 가능
    tag: Optional[str] # str이고 기본 값은 none
    date: Optional[datetime]
    some_variable_list: List[int] = [] # int로 구성된 리스트, 기본값은 []


tmp_data = {
    'mid' : '1',
    'genre' : 'action',
    'rate' : 1.5,
    'tag' : None,
    'date' : '2023-01-03 19:12:11'
}

tmp_movie = Movie(**tmp_data)
print(tmp_movie)