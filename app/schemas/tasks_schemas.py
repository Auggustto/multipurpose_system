from pydantic import BaseModel, field_validator
import re

class MetadaTasks(BaseModel):
    
    tags: str
    title: str
    description: str
    status: str
    category_id: int
    date: str
    
    @field_validator("tags")
    def validate_tags(cls, value):
        pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
        if bool(pattern.match(value)):
            return value
        else:
            raise ValueError("Tags must be in lowercase with underscore (_) as a separator.")
        
        
    @field_validator("status")
    def validate_status(cls, value):
        if value not in ["Pending", "In-Progress", "Completed"]:
            raise ValueError("Status must be one of: Pending, In Progress, Completed.")
        return value