from random import randint
from pydantic import BaseModel, Field
def generate_randam():
    return (randint(10000,99999))
class Shipment(BaseModel):
    id:str
    Contact_no:str
    Name:str=Field(max_length=60)
    Address:str=Field(default_factory=generate_randam)