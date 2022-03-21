from typing import List, Optional 

from fastapi import Depends, FastAPI, HTTPException, Header
from sqlalchemy.orm import Session 

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def welcome():
    return {"message" : "Welcome to the API"}

#### Customer

@app.post("/customers/", response_model=schemas.Customer, tags = ["Customer"])
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.get("/customers/{customer_id}", response_model=schemas.Customer, tags = ["Customer"])
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(is_done_code=404, detail="Customer not found")
    return customer
@app.delete("/customers/{customer_id}", tags = ["Customer"])
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud.remove_customer(db, customer_id=customer_id)
    return {"Status": "Successfully deleted customer"}

@app.put("/customers/{customer_id}", response_model=schemas.Customer, tags = ["Customer"])
def update_customer_info(customer_id: int, customer : schemas.Customer, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.update_customer_info(db, customer, customer_id=customer_id)
#### Store

@app.post("/stores/", response_model= schemas.Store, tags = ["Store"])
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)

@app.get("/stores/{store_id}", response_model=schemas.Store, tags = ["Store"])
def read_store(store_id: int, db: Session = Depends(get_db)):
    store = crud.get_store(db, store_id=store_id)
    if store is None:
        raise HTTPException(is_done_code=404, detail="Store not found")
    return store

#### Food 

@app.post("/foods/", response_model= schemas.Food, tags = ["Food"])
def create_food(food: schemas.FoodCreate, store_id : int, db: Session = Depends(get_db)):
    return crud.create_food(db=db, food=food, store_id=store_id)

@app.get("/foods/{food_id}", response_model=schemas.Food, tags = ["Food"])
def read_food(food_id: int, db: Session = Depends(get_db)):
    food = crud.get_food_via_id(db, food_id=food_id)
    
    if food is None:
        raise HTTPException(is_done_code=404, detail="Food not found")
    return food
@app.get("/foods/stores/{store_id}", response_model=List[schemas.Food], tags = ["Food"])
def read_food_in_the_store(store_id: int, db: Session = Depends(get_db)):
    food = crud.get_food_in_the_store(db, store_id=store_id)
    if food is None:
        raise HTTPException(is_done_code=404, detail="Food not found")
    return food

@app.put("/foods/{food_id}", response_model=schemas.Food, tags = ["Food"])
def update_food_info(food_id: int, food : schemas.Food, db: Session = Depends(get_db)):
    db_food = crud.get_food_via_id(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return crud.update_food(db, food, food_id=food_id)

@app.delete("/foods/{food_id}", tags = ["Food"])
def delete_food(food_id: int, db: Session = Depends(get_db)):
    food = crud.get_food_via_id(db, food_id=food_id)
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    crud.delete_food(db, food_id=food_id)
    return {"Status": "Successfully deleted food"}

@app.post("/foods/{food_id}", response_model=schemas.Order, tags = ["Order"])
def add_to_cart(customer_id : int, store_id : int, food_id : int, order : schemas.Order, db: Session = Depends(get_db)):
    return crud.add_to_cart(db, customer_id=customer_id, store_id=store_id, food_id=food_id, order=order)
### Order

@app.post("/orders/", response_model=schemas.Order, tags = ["Order"])
def create_order(order: schemas.OrderCreate, customer_id : int, store_id : int, food_id : int, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order, customer_id=customer_id, store_id=store_id, food_id=food_id)

@app.get("/orders/{customer_id}", tags = ["Order"])
def read_order(customer_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_via_customer_id(db, customer_id=customer_id)
    if orders is None:
        raise HTTPException(is_done_code=404, detail="Order not found")
    return orders

@app.get("/orders/stores/", tags = ["Order"])
def read_order_was_done(store_id: int, is_done : str, db: Session = Depends(get_db)):
    orders = crud.get_order_was_done(db, store_id=store_id, is_done=is_done)
    if orders is None:
        raise HTTPException(is_done_code=404, detail="Order not found")
    return orders

# @app.get("/orders/", tags = ["Order"])
# def read_order(db: Session = Depends(get_db)):
#     orders = crud.get_all_orders(db)
#     if orders is None:
#         raise HTTPException(is_done_code=404, detail="Order not found")
#     return orders

@app.put("/orders/{order_id}",response_model=List[schemas.Order], tags = ["Order"])
def update_order(order_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.update_order(db=db, order=order, order_id=order_id)




## Image

@app.post("/images/", response_model=schemas.Image, tags = ["Image"])
def create_image(image: schemas.ImageCreate, food_id : int, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image=image, food_id=food_id)

@app.get("/images/", response_model=List[schemas.Image], tags = ["Image"])
def read_image(db: Session = Depends(get_db)):
    images = crud.get_all_images(db)
    if images is None:
        raise HTTPException(is_done_code=404, detail="Image not found")
    return images
@app.get("/images/{food_id}", response_model=List[schemas.Image], tags = ["Image"])
def read_images_via_food(food_id: int, db: Session = Depends(get_db)):
    images = crud.get_images_via_food(db, food_id=food_id)
    if images is None:
        raise HTTPException(is_done_code=404, detail="Image not found")
    return images