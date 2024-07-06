from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from insurance.model.entity.base import Base


class Workers(Base):
    __tablename__ = 'workers_tbl'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _birth_date = Column("birth_date", DateTime)
    _gender = Column("gender", String(20))
    _national_id = Column("national_id", String(10))
    _email = Column("email", String(30))
    _phone_number = Column("phone_number", String(15))
    _address = Column("address", String(30))
    _deleted = Column("deleted", Boolean, default=False)

def __init__(self, name, family, birth_date, gender, national_id, email, phone, address, deleted=False):
        self._id = None
        self._name = name
        self._family = family
        self._birth_date = birth_date
        self._gender = gender
        self._national_id = national_id
        self._email = email
        self._phone_number = phone
        self._address = address
        self._deleted = deleted
