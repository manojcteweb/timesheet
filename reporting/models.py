from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    project_phase = Column(String, index=True)
    category = Column(String, index=True)

    task = relationship("Task", back_populates="reports")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    reports = relationship("Report", back_populates="task")