from xmlrpc.client import Boolean
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    address = Column(String, index=True)
    yearbirth  = Column(Integer, index = True)
    


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    address = Column(String, index=True)
  
    # orders = relationship("Order", back_populates="store")
    # foods = relationship("Food", back_populates="store")


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    quantity = Column(Integer, index=True)
    feedback = Column(String, index=True)

    # image = relationship("Image", back_populates="food")
    # store = relationship("Store", back_populates="foods")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    url = Column(String, index=True)
    food_id = Column(Integer, ForeignKey("foods.id"))


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    quantity = Column(Integer, index=True)
    total = Column(Integer, index=True)
    is_done = Column(Boolean, index=True)

    # customer = relationship("Customer", back_populates="orders")
    # store = relationship("Store", back_populates="orders")
    # food = relationship("Food", back_populates="orders")


