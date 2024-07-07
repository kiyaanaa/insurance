import re
from datetime import datetime, date


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


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text, str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_validator(message):
    def inner1(function_name):
        def inner2(self, date_param):
            if isinstance(date_param, date):
                result = function_name(self, date_param)
            elif isinstance(date_param, str):
                date_param = date_param.replace('/', '-')
                try:
                    date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
                    result = function_name(self, date_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, date):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def boolean_validator(message):
    def inner1(function_name):
        def inner2(self, bool_param):
            if isinstance(bool_param, bool):
                result = function_name(self, bool_param)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def gender_validator(function):
    def wrapper(*args, **kwargs):
        valid_genders = ["male", "female", "non-binary", "other", "prefer not to say"]
        gender = args[0]
        if gender.lower() in valid_genders:
            return function(*args, **kwargs)
        else:
            return f"Error: '{gender}' is not a valid gender."

    return wrapper


def national_id_validator(func):
    def wrapper(national_id, *args, **kwargs):
        if isinstance(national_id, str) and national_id.isdigit() and len(national_id) == 10:
            return func(national_id, *args, **kwargs)
        else:
            return f"Error: '{national_id}' is not a valid national ID. It must be a 10-digit number."

    return wrapper


def email_validator(func):
    def wrapper(email, *args, **kwargs):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            return func(email, *args, **kwargs)
        else:
            return f"Error: '{email}' is not a valid email address."

    return wrapper


def phone_number_validator(func):
    def wrapper(phone_number, *args, **kwargs):
        regex = r'^\d{11}$'
        if re.match(regex, phone_number):
            return func(phone_number, *args, **kwargs)
        else:
            return f"Error: '{phone_number}' is not a valid phone number. It must be a 11-digit number."

    return wrapper