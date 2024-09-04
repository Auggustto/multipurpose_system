from pydantic import BaseModel


class TokenData(BaseModel):
    useremail: str | None = None
    
    

