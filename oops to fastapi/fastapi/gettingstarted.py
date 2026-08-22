from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def check():
    return {"status" : "active"}


#path parameters used to identify a particular resource ; user -> user id; in url after /
@app.get("/users/{user_id}")
def users(user_id:int):
    return {"user id" : user_id,
            "username" : "rushil"
            }

@app.get("/products/{product_id}")
def products(product_id:int):
    return {"product id" : product_id}

#query parameters- in url after ? seperated by &
#1.we can normally put it in the functions as parameters 
#2.we can do multiple query parameters as well - we can predefine or user can define it as well
#3.combining path and query parameters
#difference is you can see the {} in ui whereas you cant see it in queryparameters
@app.get("/queryparameters/{example_pathparameter}")
def queryparameters(example_pathparameter : int, category : str , limit : int = 10):
    return {"example_no" : example_pathparameter,
            "categories" : category,
            "limit" : limit}


@app.get("/students/{student_id}")
def students(student_id : int , course : str , year : int):
    return {"student_id" : student_id,
            "course" : course,
            "year" : year}


#POST and request body of json
from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name :str
    age:int
    course:str

@app.post("/create_students")
def create_student(student : Student):        #inherit
    return student

#pydantic validation - request model
#1.default values - in_stock : bool = True or in_stock : str = "nope"
# 2.optional field - description : str | None = None
#selective display depends on return function   ; we can use response_model as well for bigger apis
class Products(BaseModel):
    name : str
    price : float
    category : str
    in_stock : bool = True
    secret : str
    description : str | None = None  
@app.post("/create_product")
def create_products(product : Products):
    return {"name" : product.name,
            "price" : product.price,
            "category" : product.category,
            "in_stock" : product.in_stock,
            "description" : product.description
            }
'''
this is how we use HTTPException and there are status_codes like 200,201,404,500, 400,401,403
from fastapi import HTTPException
@app.get("/students/{student_id}")
def students(student_id : int , course : str , year : int):
    if student_id not in [1,2,3]:
        raise HTTPException(status_code= 404, detail= "student not found")
    return {"student_id" : student_id,
            "course" : course,
            "year" : year}
'''

'''dependencies :
from fastapi import Depends 
def common_parameters():
    return {
        "name": "Rushil",
        "role": "student"
    }


@app.get("/profile")
def profile(user = Depends(common_parameters)):
    return user
get some grip 
'''









