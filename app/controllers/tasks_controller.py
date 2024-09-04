from app.models.tasks_models import TasksModels


class TaskController(TasksModels):
    
    def create_task(self, id: int, metadata: dict):
        return super().create_task(id, metadata)
    
    def read_task(self, id: int):
        return super().read_task(id)
    
    def update_task(self, id: int, metadata: dict):
        return super().update_task(id, metadata)
    
    def delete_task(self, id: int):
        return super().delete_task(id)