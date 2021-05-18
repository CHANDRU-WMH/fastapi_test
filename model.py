from pydantic import BaseModel, Field

## Models
class UserList(BaseModel):
    id        : str
    username  : str
    password  : str
    first_name: str
    last_name : str
    phone     : str
    gender    : str
    create_at : str
    status    : str
class UserEntry(BaseModel):
    username  : str = Field(..., example="chandru")
    password  : str = Field(..., example="Chandru@123")
    first_name: str = Field(..., example="Chandru")
    last_name : str = Field(..., example="Thillai")
    phone     : str = Field(..., example="9659903930")
    gender    : str = Field(..., example="M")
class UserUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="Chandru")
    last_name : str = Field(..., example="Thillai")
    gender    : str = Field(..., example="M")
    phone     : str = Field(..., example="9659903930")
    status    : str = Field(..., example="1")
class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")