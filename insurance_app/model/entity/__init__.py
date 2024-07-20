from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from insurance_app.model.entity.base import Base
from insurance_app.model.tools.insurance_validator import *
