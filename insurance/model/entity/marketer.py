from insurance.model.entity.__init__ import *


class Marketer(Base):
    __tablename__ = 'marketer_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
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

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid Name !!!")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid Family !!!")
    def family(self, family):
        self._family = family

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    @date_time_validator
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def gender(self):
        return self._gender

    @gender.setter
    @gender_validator
    def gender(self, gender):
        self._gender = gender

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    @national_id_validator
    def national_id(self, national_id):
        self._national_id = national_id

    @property
    def email(self):
        return self._email

    @email.setter
    @email_validator
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone_number

    @phone.setter
    @phone_number_validator
    def phone(self, phone):
        self._phone_number = phone

    @property
    def address(self):
        return self._address

    @address.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,50}$", "Invalid Address !!!")
    def address(self, address):
        self._address = address

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        if isinstance(deleted, bool):
            self._deleted = deleted
        else:
            raise ValueError("Invalid Deleted !!!")
