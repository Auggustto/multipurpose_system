from fastapi import status, HTTPException
# from sqlalchemy import desc

from app.models.database.session_db import get_db_session
from app.models.database.models import Tasks
from app.models.user_models import UserModels
from app.services.get_current_date_and_time_br_services import get_current_time
from app.models.category_models import CategoryModels



class TasksModels(UserModels):
    
    def check_user_id(self, id: int):
        return super().check_user_id(id)
    
    def check_task(self, id: int):
        with get_db_session() as db:
            return db.query(Tasks).filter(Tasks.id == id).first()
            # return db.query(Tasks).filter(Tasks.id == id).order_by(desc(Tasks.created_at)).all()
    
    
    def create_task(self, id: int, metadata: dict):
        with get_db_session() as db:
            
            check = self.check_user_id(id)
            
            if check is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Id: {id} not found.")
            
            if CategoryModels().get_category_id(int(metadata.category_id)) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id: {id} not found.")
            
            
            task = Tasks(
                tags=metadata.tags,
                title=metadata.title,
                description=metadata.description,
                user_id=check.id,
                category_id=metadata.category_id,
                status=metadata.status,
                created_at=get_current_time(),
                due_date=metadata.date
                )
            db.add(task)
            db.commit()
            return {"message": "Task added successfully"}
        
    
    def read_task(self, id: int):
        check = self.check_task(id)
        
        if check is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id: {id} not found.")
        return check.as_dict()
    
    
    def update_task(self, id: int, metadata: dict):
        with get_db_session() as db:
            
            check = self.check_task(id)
            
            if check is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id: {id} not found.")
            
            check.tags = metadata.tags
            check.title = metadata.title
            check.description = metadata.description
            check.status = metadata.status
            check.updated_at = get_current_time()
            db.add(check)
            db.commit()
            return {"message": "Task updated successfully"}
        
        
    def delete_task(self, id: int):
        with get_db_session() as db:
            
            check = self.check_task(id)
            
            if check is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id: {id} not found.")
            
            db.delete(check)
            db.commit()
            return {"message": "Task deleted successfully"}