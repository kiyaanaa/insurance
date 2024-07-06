from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from insurance.model.entity.base import Base


class Insurances(Base):
    __tablename__ = 'insurances_tbl'
    _selling_id = Column(Integer, ForeignKey=True, autoincrement=True)
    _insurance_id = Column(Integer, ForeignKey=True, autoincrement=True)
    _worker_id = Column(Integer, ForeignKey=True, autoincrement=True)
    _name = Column("name", String(30))
    _date_of_sale = Column("date_of_sale", DateTime)
    _price = Column("price", Integer)

def __init__(self, name, date_of_sale, price):
    self._id = None
    self._name = name
    self._date_of_sale = date_of_sale
    self._price = price