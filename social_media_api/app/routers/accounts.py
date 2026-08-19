from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.accounts import AccountsCreate, AccountResponse
from app.models.accounts import Account
from fastapi import HTTPException


router = APIRouter()


@router.post("/accounts" , status_code= 201, response_model= AccountResponse)
def create_account(account : AccountsCreate , db : Session = Depends(get_db)): #account creating and session
    new_account = Account(                                  #from the table base model to new object attributes of sqlalchemy
        username = account.username,
        email = account.email,
        password = account.password,
        full_name = account.full_name,
        bio = account.bio,
    )   
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

@router.get("/accounts", response_model = list[AccountResponse])
def get_accounts(db:Session = Depends(get_db)): 
    accounts = db.query(Account).all()        #query(Account).all() -> fetching all data from the database(Account class has db table)
    return accounts 



@router.get("/accounts/{account_id}" , response_model = AccountResponse)
def get_an_account(account_id : int , db : Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:                                                           #finding account
        raise HTTPException(status_code= 404, detail = "No ID found")
    return account


@router.put("/accounts/{account_id}" , response_model = AccountResponse)
def update_an_account(account_id : int , updated_account : AccountsCreate , db : Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:
        raise HTTPException(status_code= 404, detail = "No ID found")

    account.username = updated_account.username,
    account.email = updated_account.email,
    account.password = updated_account.password,
    account.full_name = updated_account.full_name,
    account.bio = updated_account.bio

    db.commit() 
    db.refresh(account)
    return account

@router.delete("/accounts/{account_id}" , response_model = AccountResponse)
def delete_an_account(account_id : int , db : Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:
        raise HTTPException(status_code= 404, detail = "No ID found")

    db.delete(account)
    db.commit()

    return account




