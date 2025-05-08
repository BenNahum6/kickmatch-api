from sqlalchemy import Column, Integer, String
from app.db.database_sqlalchemy import Base  # <<< לא מה-Supabase Client!

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
