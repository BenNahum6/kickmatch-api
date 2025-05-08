from sqlalchemy import Column, Integer, String, Boolean
from app.db.database_sqlalchemy import Base

class PlayerGame(Base):
    __tablename__ = 'player_game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    team = Column(String(1), nullable=False)  # Group - 'A' or 'B'
