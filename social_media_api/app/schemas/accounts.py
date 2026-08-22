from pydantic import BaseModel
class AccountsCreate(BaseModel):
    username : str 
    email : str
    password:str
    full_name : str
    bio : str | None = None
class AccountResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    bio: str | None = None
    is_active: bool

    
    class Config:
        from_attributes = True   #It tells Pydantic:

#"I may give you a SQLAlchemy object instead of a normal dictionary."
#" Read its attributes and turn them into this response model."

#relations
class PostCreate(BaseModel):
    content : str

class PostResponse(BaseModel):
    id : int
    content : str 
    account_id : int

    class Config:
        from_attributes = True


#security 
class LoginRequest(BaseModel):
    username : str
    password : str

    

