from fastapi import status, HTTPException
from datetime import timedelta
from datetime import timedelta

from fastapi import HTTPException, status
from app.models.user_models import UserModels
from app.services.password_services import validation_password
from app.services.create_token_services import create_access_token



class UserLoginModels(UserModels):

    # @catch_exceptions
    def user_login(self, metadata):
        
        user = super().check_user_email(metadata.email)
        ACCESS_TOKEN_EXPIRE_MINUTES = 30

        if user:
            
            ### Validation password ###
            if validation_password(password=metadata.password, password_registred=user.password):
                
                ### Create token ###
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(
                    data={"sub": user.name}, expires_delta=access_token_expires
                )
                return {"id": user.id, "token": access_token}
            
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email or password is incorrect")