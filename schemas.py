from typing import List, Optional

from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    id : int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    yearbirth: Optional[int] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    class Config:
        orm_mode = True

class StoreBase(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    class Config:
        orm_mode = True


class FoodBase(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
    feedback : str 

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    store_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    id: int
    quantity: int
    total: int
    is_done : bool = False

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    customer_id: int
    store_id: int
    food_id : int

    class Config:
        orm_mode = True


class ImageBase(BaseModel):
    id : int
    url: str
    

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    food_id: int
    class Config:
        orm_mode = True