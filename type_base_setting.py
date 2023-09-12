from typing import List, Optional, Union
from datetime import datetime

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    # 여기에 지정된 필드 타입의 값으로 읽어옴
    db_host: str = Field(default='127.0.0.1', env='db_host')
    db_port: int = Field(default=3306, env='db_port')

    class Config:
        env_file = '.env'

    @field_validator("db_port")
    def check_port(cls, port_input):
        if port_input not in [3306, 8080]:
            raise ValueError("port error")
        return port_input

config = DBConfig()
print(config.model_dump())