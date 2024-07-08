from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from insurance.model.entity.base import Base
from insurance.model.tools.insurance_validator import pattern_validator, date_time_validator


class Insurances(Base):
    __tablename__ = 'insurances_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _insurance_id = Column("insurance_id", String(30))
    _worker_id = Column("worker_id", Integer)
    _name = Column("name", String(30))
    _date_of_sale = Column("date_of_sale", DateTime)
    _price = Column("price", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, date_of_sale, price, deleted=False):
        self._id = None
        self._insurance_id = None
        self._worker_id = None
        self._name = name
        self._date_of_sale = date_of_sale
        self._price = price
        self._deleted = deleted

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid Name !!!")
    def name(self, name):
        self._name = name

    @property
    def date_of_sale(self):
        return self._date_of_sale

    @date_of_sale.setter
    @date_time_validator
    def date_of_sale(self, date_of_sale):
        self._date_of_sale = date_of_sale

    @property
    def price(self):
        return self._price

    @price.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid Price !!!")
    def price(self, price):
        self._price = price

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        if isinstance(deleted, bool):
            self._deleted = deleted
        else:
            raise ValueError("Invalid Deleted !!!")
