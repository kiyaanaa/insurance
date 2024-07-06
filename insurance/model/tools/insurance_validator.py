import re
from datetime import datetime

class InsuranceValidator:
    @staticmethod
    def insured_validator(insured, message):
        if isinstance(insured, str) and re.match(r"^[a-zA-Z\s]{2,30}$", insured, re.IGNORECASE):
            return insured
        else:
            raise ValueError(message)

    @staticmethod
    def employee_validator(employee, message):
        if isinstance(employee, str) and re.match(r"^[a-zA-Z\s]{2,30}$", employee, re.IGNORECASE):
            return employee
        else:
            raise ValueError(message)

    @staticmethod
    def marketer_validator(marketer, message):
        if isinstance(marketer, str) and re.match(r"^[a-zA-Z\s]{2,30}$", marketer, re.IGNORECASE):
            return marketer
        else:
            raise ValueError(message)

    @staticmethod
    def representative_validator(representative, message):
        if isinstance(representative, str) and re.match(r"^[a-zA-Z\s]$", representative, re.IGNORECASE):
            return representative
        else:
            raise ValueError(message)

    @staticmethod
    def price_validator(price, message):
        if isinstance(price, int):
            return price
        else:
            raise ValueError(message)

    @staticmethod
    def date_time_validator(date_time_value, message):
        if isinstance(date_time_value, datetime):
            return date_time_value
        else:
            raise ValueError(message)
