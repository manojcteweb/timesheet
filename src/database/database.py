from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Example for SQLite
# For PostgreSQL, use: 'postgresql://user:password@postgresserver/db'

# Create a new SQLAlchemy engine instance
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our classes definitions
Base = declarative_base()

# Dependency to get the session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()