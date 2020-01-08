from pydantic import BaseModel
from sqlalchemy import VARCHAR,FLOAT


class User(BaseModel):
    pincode: str
    address: str
    city: str
    latitude: float
    longitude: float


class Userout(BaseModel):
    pincode: str
    address: str
    city: str


class Userin(BaseModel):
    latitude: float
    longitude: float
