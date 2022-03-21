from ntpath import join
from typing import Optional
from sqlalchemy.orm import Session

from . import models, schemas

############ Customer ############

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def create_customer(db: Session, customer : schemas.CustomerCreate):
    # db_customer = models.Customer(**customer.dict())
    db_cus = models.Customer(name = customer.name,
    email = customer.email,
    phone = customer.phone,
    address = customer.address,
    yearbirth = customer.yearbirth)

    db.add(db_cus)
    db.commit()
    db.refresh(db_cus)
    return db_cus

def remove_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    db.delete(customer)
    db.commit()
    return customer

def update_customer_info(db: Session, customer : schemas.Customer, customer_id : int):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    db_customer.name = customer.name
    db_customer.email = customer.email
    db_customer.phone = customer.phone
    db_customer.address = customer.address
    db_customer.yearbirth = customer.yearbirth
    db.commit()
    db.refresh(db_customer)
    return db_customer

############ Store ############

def get_store(db: Session, store_id : int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

def create_store(db : Session, store : schemas.StoreCreate):
    db_store = models.Store(name = store.name,
                            address = store.address,
                            phone = store.phone,
                            email = store.email)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store
# Get the order was done 
def get_order_was_done(db: Session, store_id : int , is_done : str):
    return db.query(models.Order).filter(models.Order.is_done == str(is_done) and models.Order.store_id == store_id).all()
# Food

def get_food_via_id(db: Session, food_id : int):
    return db.query(models.Food).filter(models.Food.id == food_id).first()


def create_food(db: Session, food : schemas.FoodCreate, store_id : int):
    db_food = models.Food(
                            name = food.name,
                            price = food.price,
                            quantity = food.quantity,
                            feedback = food.feedback,
                            store_id=store_id)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

# Get all food in the store
def get_food_in_the_store(db: Session, store_id : int):
    return db.query(models.Food).filter(models.Food.store_id == store_id).all()

def delete_food(db: Session, food_id : int):
    food = db.query(models.Food).filter(models.Food.id == food_id).first()
    db.delete(food)
    db.commit()
    return food

def update_food(db: Session, food : schemas.Food, food_id : int):
    db_food = db.query(models.Food).filter(models.Food.id == food_id).first()
    db_food.name = food.name
    db_food.price = food.price
    db_food.quantity = food.quantity
    db.commit()
    db.refresh(db_food)
    return db_food

def add_to_cart(db: Session, order : schemas.OrderCreate, customer_id : int, store_id : int, food_id : int):
    
    db_food = db.query(models.Food).filter(models.Food.id == food_id).first()
    db_order = models.Order(
                            id = order.id,
                            total = order.quantity * db_food.price, 
                            food_id = food_id, 
                            quantity = order.quantity, 
                            is_done = order.is_done, 
                            customer_id = customer_id, 
                            store_id=store_id
                            )
    db_food.quantity = db_food.quantity - order.quantity

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# def add_to_cart_already(db: Session, order : schemas.OrderCreate, customer_id : int, food_id : int):
#     db_order = db.query(models.Order).filter(models.Order.id == )
# Order
def get_all_orders(db: Session):
    return db.query(models.Order).all()
    

def get_order_via_customer_id(db: Session, customer_id : int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()

def create_order(db: Session, order : schemas.OrderCreate, customer_id : int, store_id : int, food_id : int):
    db_order = models.Order(
                            total = order.total, 
                            food_id = food_id, 
                            quantity = order.quantity, 
                            is_done = order.is_done, 
                            customer_id = customer_id, 
                            store_id=store_id
                            )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order : schemas.Order, order_id : int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    db_order.total = order.total
    db_order.quantity = order.quantity
    db_order.is_done = order.is_done
    db.commit()
    db.refresh(db_order)
    return db_order

### Image

def create_image(db: Session, image : schemas.ImageCreate, food_id : int):
    db_image = models.Image(url = image.url, food_id=food_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_all_images(db: Session):
    return db.query(models.Image).all()

def get_images_via_food(db: Session, food_id: int):
    return db.query(models.Image).filter(models.Image.food_id == food_id).all()