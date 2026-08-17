from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter()
@router.get("/accounts")
def get_accounts(db:Session = Depends(get_db)):
    return {"message" : "routers check"}
