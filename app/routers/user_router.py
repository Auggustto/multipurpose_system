from fastapi import APIRouter, status, Depends
from app.controllers.user_controller import UserController
from app.schemas.user_schemas import MetadaUser
from app.services.create_token_services import validation_token

user_routers = APIRouter(prefix='/task-schedule/api', tags=['Users'])

@user_routers.post('/user', status_code=status.HTTP_201_CREATED, tags=['Users'])
def create(metadata: MetadaUser):
    return UserController().create_user(metadata)

@user_routers.get('/user/{id}', status_code=status.HTTP_200_OK, tags=['Users'])
def read(id: int, current_user: str = Depends(validation_token)):
    return UserController().read_user(id)

@user_routers.put('/user/{id}', status_code=status.HTTP_200_OK, tags=['Users'])
def update(id: int, metadata: MetadaUser, current_user: str = Depends(validation_token)):
    return UserController().update_user(id, metadata)

@user_routers.delete('/user/{id}', status_code=status.HTTP_201_CREATED, tags=['Users'])
def delete(id: int, current_user: str = Depends(validation_token)):
    return UserController().delete_user(id)