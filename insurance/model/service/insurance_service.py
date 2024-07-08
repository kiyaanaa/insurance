from insurance.controller.exception.insurance_exception import InsuranceNotFoundError
from insurance.model.da.insurance_da import DataAccess
from insurance.model.entity.insured import Insurance
class InsuranceService:
    @staticmethod
    def save(insurance):
        insurance_da = DataAccess(Insurance)
        insurance_da.save(insurance)
        return insurance

    @staticmethod
    def edit(insurance):
        insurance_da = DataAccess(Insurance)
        if insurance_da.find_by_id(insurance.id):
            insurance_da.edit(insurance)
            return insurance
        else:
            raise InsuranceNotFoundError()

    @staticmethod
    def remove(id):
        insurance_da = DataAccess(Insurance)
        if insurance_da.find_by_id(id):
            return insurance_da.remove(id)
        else:
            raise InsuranceNotFoundError()

    @staticmethod
    def find_all():
        insurance_da = DataAccess(Insurance)
        return insurance_da.find_all()

    @staticmethod
    def find_by_id(id):
        insurance_da = DataAccess(Insurance)
        return insurance_da.find_by_id(id)
