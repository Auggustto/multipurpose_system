from pydantic import BaseModel, EmailStr

class MetadaUserLogin(BaseModel):
    
    email: EmailStr
    password: str