from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, Date
from insurance.model.entity.base import Base
from insurance.model.tools.insurance_validator import *


class InsuranceSell(Base):
    __tablename__ = 'insurance_sell_tbl'
    _id = Column("id", Integer, ForeignKey=True, autoincrement=True)
    _person_id = Column("person_id", Integer)
    _insured_id = Column("insurance_id", Integer)
    _start_date = Column("start_date", Date)
    _end_date = Column("end_date", Date)
    _date_of_sale = Column("date_of_sale", DateTime)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, start_date, end_date, date_of_sale, deleted=False):
        self._id = None
        self._person_id = None
        self._insured_id = None
        self._start_date = start_date
        self._end_date = end_date
        self._date_of_sale = date_of_sale
        self._deleted = deleted

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    @date_time_validator
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    @date_time_validator
    def end_date(self, value):
        self._end_date = value

    @property
    def date_of_sale(self):
        return self._date_of_sale

    @date_of_sale.setter
    @date_time_validator
    def date_of_sale(self, value):
        self._date_of_sale = value

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    @deleted
    def deleted(self, deleted):
        if isinstance(deleted, bool):
            self._deleted = deleted
        else:
            raise ValueError("Invalid Deleted !!!")
