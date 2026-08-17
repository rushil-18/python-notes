from sqlalchemy import Column , Integer , Text , Boolean , String
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)

    