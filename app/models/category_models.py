from fastapi import status, HTTPException
from sqlalchemy.exc import IntegrityError


from app.models.database.session_db import get_db_session
from app.models.database.models import Category

class CategoryModels(Category):
    
    def get_category_id(self, id: int):
        with get_db_session() as db:
            return db.query(Category).filter_by(id=id).first()
    
    def get_category(self, category: str):
        with get_db_session() as db:
            return db.query(Category).filter_by(category=category).first()
        
    
    def create_category(self, metadata: dict):
        with get_db_session() as db:
            
            check = self.get_category(str(metadata.category).upper())
            
            if check is not None:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Category: {metadata.category} already registered")
            
            task = Category(
                category=str(metadata.category).upper()
                )
            db.add(task)
            db.commit()
            return {"message": "Category added successfully"}
    
    
    def read_category(self, id: int):
        
        check = self.get_category_id(id)
        
        if check is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id: {id} not found.")
        return check.as_dict()
    
    
    def update_category(self, id: int, metadata: dict):
        
        with get_db_session() as db:
        
            check = self.get_category_id(id)
            
            if check is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id: {id} not found.")
            
            if self.get_category(str(metadata.category).upper()) is not None:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Category: {metadata.category} already registered")     
            
            cat = str(metadata.category).upper()
            print(cat)
            check.category = cat
            db.add(check)
            db.commit()
            return {"message": "Category updated successfully"}
    
        
    def delete_category(self, id: int):
        with get_db_session() as db:
            
            check = self.get_category_id(id)
            
            if check is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id: {id} not found.")
            
            db.delete(check)
            db.commit()
            return {"message": "Category deleted successfully"}


    def read_all(self):
        with get_db_session() as db:
            return db.query(Category).all()