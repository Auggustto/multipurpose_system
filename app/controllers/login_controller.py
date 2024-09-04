from app.models.login_models import UserLoginModels


class UserLoginController(UserLoginModels):
    
    def user_login(self, metadata):
        return super().user_login(metadata)