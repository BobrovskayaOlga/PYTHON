from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    course = Column(String(50), nullable=False)
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}', course='{self.course}')>"
