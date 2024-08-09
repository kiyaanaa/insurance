from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# تعریف Base و engine
DATABASE_URL = "sqlite:///personal_database.db"  # آدرس پایگاه داده SQLite

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class PersonalInfo(Base):
    __tablename__ = 'personal_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    national_code = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)


# ایجاد جدول‌ها در پایگاه داده
Base.metadata.create_all(engine)
