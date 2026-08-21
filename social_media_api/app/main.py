from fastapi import FastAPI
from app.routers.accounts import router as account_router


from app.database import engine, Base
from app.models.accounts import Account , Posts


app = FastAPI()
@app.get("/")
def working():
    return {"server" : "OK"}
app.include_router(account_router)
Base.metadata.create_all(bind= engine)

