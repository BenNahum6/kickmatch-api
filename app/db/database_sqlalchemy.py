from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
SessionLocal = None
engine = None

def init_engine(database_url: str):
    global engine, SessionLocal
    engine = create_engine(database_url, connect_args={"sslmode": "require"})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
