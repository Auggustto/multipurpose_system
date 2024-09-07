from sqlalchemy import Integer, String, Column, DateTime, Boolean, LargeBinary, ForeignKey, func, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.database.base import Base
from app.services.get_current_date_and_time_br_services import format_datetime
from collections import Counter
from sqlalchemy import desc


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String, nullable=False)
    account_status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=True, default=func.now())
    updated_at = Column(DateTime, nullable=True)
    
    # tasks = relationship("Tasks", back_populates="user", order_by=desc("tasks.created_at"))
    tasks = relationship("Tasks", back_populates="user")
    accounts = relationship("Accounts", back_populates="user")
    
    
    def as_dict(self):

        status_count = Counter(task.status for task in self.tasks)
                
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "account_status": self.account_status,
            "tasks": [task.as_dict() for task in self.tasks],
            "status_count": dict(status_count)
        }
        

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    tags = Column(String(15), unique=False)
    title = Column(String(50), unique=False)
    description = Column(String, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    status = Column(String, unique=False)
    
    # created_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    due_date = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "tags": self.tags,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "categorie_id": self.category_id,
            "status": self.status,
            "created_at": self.format_datetime(self.created_at),
            "due_date": self.format_datetime(self.due_date),
            "updated_at": self.updated_at
        }
    
    @staticmethod
    def format_datetime(value):
        if value:
            return value.strftime("%d/%m/%Y %H:%M:%S")
        return None

class Accounts(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(100), nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="accounts")


class Category(Base):
    
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    category = Column(String(50), unique=True)
    type = Column(String(20), nullable=False, default='')
    
    tasks = relationship("Tasks", back_populates="category")
    
    def as_dict(self):
        return {
            "id": self.id,
            "tags": self.category,
        }