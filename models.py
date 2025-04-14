from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    available = Column(Boolean, default=True)
    skill = Column(String, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="resources")


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    resources = relationship("Resource", back_populates="project")