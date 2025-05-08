from sqlalchemy import Column, Integer, String, Boolean
from app.db.database_sqlalchemy import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    regular_player = Column(Boolean, nullable=False, default=False)
