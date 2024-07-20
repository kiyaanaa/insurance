from insurance_app.controller import *


class InsuranceController:
    @classmethod
    @exception_handling
    def save(cls, name, date_of_sale, price):
        insurance = Insurance(name, date_of_sale, price)
        return True, InsuranceService.save(insurance)

    @classmethod
    @exception_handling
    def edit(cls, id, insurance_id, worker_id, name):
        insurance = Insurance(id, insurance_id, worker_id, name)
        insurance.id = id
        return True, InsuranceService.edit(insurance)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, InsuranceService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, InsuranceService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, InsuranceService.find_by_id(id)


class InsuranceSellController:
    @classmethod
    @exception_handling
    def save(cls, start_date, end_date, date_of_sale):
        insurance_sell = InsuranceSell(start_date, end_date, date_of_sale)
        return True, InsuranceService.save(insurance_sell)

    @classmethod
    @exception_handling
    def edit(cls, id, person_id, insured_id):
        insurance_sell = InsuranceSell(id, person_id, insured_id)
        insurance_sell.id = id
        return True, InsuranceSellService.edit(insurance_sell)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, InsuranceSellService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, InsuranceSellService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, InsuranceSellService.find_by_id(id)


class InsuredController:
    @classmethod
    @exception_handling
    def save(cls, name, family, birth_date, gender, national_id, email, phone, address):
        insured = Insured(name, family, birth_date, gender, national_id, email, phone, address)
        return True, InsuranceService.save(insured)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, birth_date, gender, national_id, email, phone, address):
        insured = Insured(id, name, family, birth_date, gender, national_id, email, phone, address)
        insured.id = id
        return True, InsuredService.edit(insured)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, InsuredService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, InsuredService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, InsuredService.find_by_id(id)


class MarketerController:
    @classmethod
    @exception_handling
    def save(cls, name, family, birth_date, gender, national_id, email, phone, address):
        marketer = Marketer(name, family, birth_date, gender, national_id, email, phone, address)
        return True, MarketerService.save(marketer)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, birth_date, gender, national_id, email, phone, address):
        marketer = Marketer(id, name, family, birth_date, gender, national_id, email, phone, address)
        marketer.id = id
        return True, MarketerService.edit(marketer)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, MarketerService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, MarketerService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, MarketerService.find_by_id(id)


class WorkerController:
    @classmethod
    @exception_handling
    def save(cls, name, family, birth_date, gender, national_id, email, phone, address):
        worker = Worker(name, family, birth_date, gender, national_id, email, phone, address)
        return True, WorkerService.save(worker)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, birth_date, gender, national_id, email, phone, address):
        worker = Worker(id, name, family, birth_date, gender, national_id, email, phone, address)
        worker.id = id
        return True, WorkerService.edit(worker)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, WorkerService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, WorkerService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, WorkerService.find_by_id(id)