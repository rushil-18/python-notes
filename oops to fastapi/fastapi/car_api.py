from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
app = FastAPI()



class Car(BaseModel):
    id : int
    company : str
    model : str
    price : float
    years_used : float
    in_stock : bool
    password : int
class CarResponse(BaseModel):
    id : int
    company : str
    model : str
    price : float
    years_used : float
    in_stock : bool

automobiles = []

#creating a car/ adding a car
@app.post("/Add_cars" , status_code= 201 , response_model= CarResponse)
def add_cars(car : Car):        #inheriting the base model
    automobiles.append(car)
    return car
#get all
@app.get("/cars_available" , response_model= list[CarResponse])
def get_cars():
    return automobiles
#get by id 
@app.get("/cars_by_id/{car_id}" , response_model= CarResponse)
def get_cars_by_id(car_id : int):
    for automobile in automobiles:
        if automobile.id == car_id:
            return automobile

    raise HTTPException(status_code=404, detail= "No car found by id")
#update 
@app.put("/update_cars/{car_id}", response_model= CarResponse)
def updatecars(car_id : int, updated_car : Car):
    for index, automobile in enumerate(automobiles):
        if automobile.id == car_id:
            automobiles[index] = updated_car
            return updated_car

    raise HTTPException(status_code= 404, detail= "No car found by id")

#delete 
@app.delete("/delete cars/{car_id}" , response_model= CarResponse)
def delete_cars(car_id : int):
    for index , automobile in enumerate(automobiles):
        if automobile.id == car_id:
            deleted_car = automobiles.pop(index)
            return deleted_car

    raise HTTPException (status_code = 404, detail = "No car found by id")




    


