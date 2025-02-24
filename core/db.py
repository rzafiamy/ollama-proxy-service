from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database file
DATABASE_URL = "sqlite:///monitoring.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=False)

# Define a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

class RequestLog(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    endpoint = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    user_id = Column(String, nullable=False)

def init_db():
    """Initialize the database and create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)

# Call this when initializing the app
init_db()
