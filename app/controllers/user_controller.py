from app.models.user_models import UserModels
from app.services.validator_email_services import validation_format_email


class UserController(UserModels):
    
    def create_user(self, metadata):
        return super().create_user(metadata)
    
    def read_user(self, id: int):
        # if validation_format_email(id):
        return super().read_user(id)
        
    def update_user(self, id: int, metadata):
        # if validation_format_email(id):
        return super().update_user(id, metadata)
    
    def delete_user(self, id: int):
        # if validation_format_email(email):
        return super().delete_user(id)