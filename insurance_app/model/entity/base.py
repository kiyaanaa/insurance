from insurance_app.model.entity import *


class Base(DeclarativeBase):
    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})