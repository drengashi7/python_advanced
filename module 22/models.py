from babel.messages.pofile import escape
from pydamtic import BaseModel,FieldaValidationInfo, field_validator,cons

class User(BaseModel)
    id:int
    name:str
    age:int

    @field_validator('age')
    def age_must_be_positive(cls,v,info:FieldaValidationInfo):
        if v <=0:
            raise ValueError('Age must be positive')
        return v

try:
    user = User(id=1, name ="stina", age=15)
except ValueError as e:
    Print(e)

class Address(BaseModel):
    street:str
    city:str