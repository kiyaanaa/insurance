from insurance.model.entity.insured import Insurance
from insurance.model.service.insurance_service import InsuranceService
from insurance.model.tools import logger
from insurance.model.tools.logger import Logger


class InsuranceController:
    @staticmethod
    def save(insured, employee, marketer, representative, price, insurance_date_time):
        try:
            insurance = Insurance(insured, employee, marketer, representative, price, insurance_date_time)
            InsuranceService.save(insurance)
            logger.info(f"Insurance Saved - {insurance}")
            return True, insurance
        except Exception as e:
            logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(insured, employee, marketer, representative, price, insurance_date_time):
        try:
            insurance = Insurance(insured, employee, marketer, representative, price, insurance_date_time)
            InsuranceService.edit(insurance)
            logger.info(f"Insurance Edited - {insurance}")
            return True, insurance
        except Exception as e:
            logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            insurance = InsuranceService.remove(id)
            Logger.info(f"Insurance Removed - {insurance}")
            return True, insurance
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            insurance_list = InsuranceService.find_all()
            Logger.info(f"Insurance Find All()")
            return True, insurance_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            insurance = InsuranceService.find_by_id(id)
            Logger.info(f"Insurance Find By Id({id})")
            return True, insurance
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


