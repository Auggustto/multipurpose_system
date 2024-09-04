from fastapi import APIRouter, status
from app.controllers.login_controller import UserLoginController
from app.schemas.user_login_schemas import MetadaUserLogin

user_login_routers = APIRouter(prefix='/api/devel/multipurpose_system/user', tags=['Users'])

@user_login_routers.post('/login', status_code=status.HTTP_200_OK, tags=['Users'])
def create(metadata: MetadaUserLogin):
    return UserLoginController().user_login(metadata)