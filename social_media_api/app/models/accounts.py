from sqlalchemy import Column , Integer , Text , Boolean , String, ForeignKey
from sqlalchemy.orm import relationship
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
    posts = relationship("Posts",back_populates= "account")


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer , primary_key= True , index= True)
    content = Column(String , nullable = False)
    account_id = Column(Integer , ForeignKey("accounts.id"), nullable = False)
    account = relationship("Account" , back_populates= "posts")