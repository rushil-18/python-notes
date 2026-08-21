from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.accounts import AccountsCreate, AccountResponse
from app.schemas.accounts import PostCreate, PostResponse
from app.models.accounts import Account
from app.models.accounts import Posts
from fastapi import HTTPException
from app.security import hash_password , verify_password

router = APIRouter()


@router.post("/accounts" , status_code= 201, response_model= AccountResponse)
def create_account(account : AccountsCreate , db : Session = Depends(get_db)): #account creating and session
    new_account = Account(                                  #from the table base model to new object attributes of sqlalchemy
        username = account.username,
        email = account.email,
        password = hash_password(account.password),
        full_name = account.full_name,
        bio = account.bio
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


#posts
@router.post("/accounts/{account_id}/posts" , status_code = 201 , response_model = PostResponse)
def create_post(account_id : int, post : PostCreate , db : Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:
        raise HTTPException(status_code= 404 , detail = "No Account")

    new_post = Posts(content = post.content, account_id = account_id )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#get all posts
@router.get("/posts" ,response_model = list[PostResponse])
def get_all_posts(db : Session = Depends(get_db)):
    posts = db.query(Posts).all()
    return posts


@router.get("/accounts/{account_id}/posts" , response_model = list[PostResponse])
def get_posts(account_id : int , db : Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()              #finding if an account exists
    if account is None:
        raise HTTPException(status_code= 404 , detail = "No Account")
    all_posts = db.query(Posts).filter(Posts.account_id == account_id).all()
    return all_posts


@router.get("/posts/{post_id}" , response_model = PostResponse)
def get_post(post_id : int, db : Session = Depends(get_db)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if post is None:
        raise HTTPException(status_code = 404 , detail = "No post found")
    return post


@router.put("/posts/{post_id}"  ,response_model = PostResponse)
def update_posts(post_id : int , new_updated_post : PostCreate , db : Session = Depends(get_db)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if post is None: 
        raise HTTPException(status_code= 404 , detail = "No post")

    post.content = new_updated_post.content
    db.commit() 
    db.refresh(post)

    return post

@router.delete("/posts/{post_id}")
def delete_post(post_id : int , db : Session = Depends(get_db)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if post is None:
        raise HTTPException(status_code = 404 , detail = "No post found")

    db.delete(post)
    db.commit() 
    return post

