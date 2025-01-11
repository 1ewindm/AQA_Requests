from pydantic import BaseModel, field_validator
from typing import List

class MetaModel(BaseModel):
    total: int

class UserModel(BaseModel):

    email: str
    name: str
    nickname: str
    uuid: str

class AllUserModel(BaseModel):
    meta: MetaModel
    users: List[UserModel]  # Изменено на список пользователей


