from typing import List, Optional, Union
from datetime import datetime

from pydantic import Field, field_validator, BaseModel
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    # 여기에 지정된 필드 타입의 값으로 읽어옴
    db_host: str = Field(default='127.0.0.1', env='db_host')
    db_port: int = Field(default=3306, env='db_port')

    class Config:
        env_file = '.env'

    # v1 : @validator('host', pre=True)
    @field_validator('host', mode='before', check_fields=False)
    def check_host(cls, host_input):
        if host_input == 'localhost':
            return "127.0.0.1"
        return host_input

    @field_validator('db_port', check_fields=False)
    def check_port(cls, port_input):
        if port_input not in [3306, 8080]:
            raise ValueError("port error")
        return port_input
    


class ProjectConfig(BaseModel):
    project_name: str = 'fast api'
    db_info: DBConfig = DBConfig()


data = {
    'project_name': 'fast api',
    'db_info' : {
        'db_host' : 'localhost',
        'db_port' : 3306
    }
}


project = ProjectConfig(**data)
print(project.model_dump())
print(project.db_info)