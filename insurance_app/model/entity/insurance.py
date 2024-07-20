from insurance_app.model.entity.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from insurance_app.model.tools.insurance_validator import *


class Insurance(Base):
    __tablename__ = 'insurance_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _insurance_id = Column("insurance_id", Integer)
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
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def worker_id(self):
        return self._id

    @id.setter
    def worker_id(self, id):
        self._id = id

    @property
    def insurance_id(self):
        return self._id

    @id.setter
    def insurance_id(self, id):
        self._id = id

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
