from pydantic import BaseModel, field_validator, constr

class MetadaCategory(BaseModel):
    
    category: constr(min_length=1, max_length=10)
