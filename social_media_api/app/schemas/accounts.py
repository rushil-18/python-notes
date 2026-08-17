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

    
