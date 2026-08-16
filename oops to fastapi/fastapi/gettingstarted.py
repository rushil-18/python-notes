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
class Student(BaseModel):
    name :str
    age:int
    course:str

@app.post("/create_students")
def create_student(student : Student):        #inherit
    return student


class Products(BaseModel):
    name : str
    price : float
    catrgory : str
    in_stock : bool
    secret : str                          #now you dont want to show secret do u so you can do product.name, product.price and whatev you like to show

@app.post("/create_product")
def create_products(product : Products):
    return product
                








