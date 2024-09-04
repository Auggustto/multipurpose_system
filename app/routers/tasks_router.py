from fastapi import APIRouter, status, Depends
from app.controllers.tasks_controller import TaskController
from app.schemas.tasks_schemas import MetadaTasks
from app.services.create_token_services import validation_token

tasks_routers = APIRouter(prefix='/api/devel/multipurpose_system', tags=['Tasks'])

@tasks_routers.post('/task/{id}', status_code=status.HTTP_201_CREATED, tags=['Tasks'])
def create(id: int, metadata: MetadaTasks, current_user: str = Depends(validation_token)):
    return TaskController().create_task(id, metadata)

@tasks_routers.get('/task/{id}', status_code=status.HTTP_200_OK, tags=['Tasks'])
def read(id: int, current_user: str = Depends(validation_token)):
    return TaskController().read_task(id)

@tasks_routers.put('/task/{id}', status_code=status.HTTP_200_OK, tags=['Tasks'])
def update(id: int, metadata: MetadaTasks, current_user: str = Depends(validation_token)):
    return TaskController().update_task(id, metadata)

@tasks_routers.delete('/task/{id}', status_code=status.HTTP_200_OK, tags=['Tasks'])
def delete(id: int, current_user: str = Depends(validation_token)):
    return TaskController().delete_task(id)