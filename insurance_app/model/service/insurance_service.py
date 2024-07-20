from insurance_app.model.service import *


class InsuranceService:
    @classmethod
    def save(cls, insurance):
        insurance_da = DataAccess(insurance)
        insurance_da.save(insurance)
        return insurance

    @classmethod
    def edit(cls, insurance):
        insurance_da = DataAccess(insurance)
        if insurance_da.find_by_id(insurance.id):
            insurance_da.edit(insurance)
            return insurance
        else:
            raise InsuranceNotFoundError()

    @classmethod
    def remove(cls, id):
        insurance_da = DataAccess(insurance)
        if insurance_da.find_by_id(id):
            return insurance_da.remove(id)
        else:
            raise InsuranceNotFoundError()

    @classmethod
    def find_all(cls, ):
        insurance_da = DataAccess(insurance)
        return insurance_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        insurance_da = DataAccess(insurance)
        return insurance_da.find_by_id(id)


class InsuredService:
    @classmethod
    def save(cls, insured):
        insured_da = DataAccess(Insured)
        insured_da.save(insured)
        return insured

    @classmethod
    def edit(cls, insured):
        insured_da = DataAccess(Insured)
        if insured_da.find_by_id(insured.id):
            insured_da.edit(insured)
            return insured
        else:
            raise InsuredNotFoundError()

    @classmethod
    def remove(cls, id):
        insured_da = DataAccess(Insured)
        if insured_da.find_by_id(id):
            return insured_da.remove(id)
        else:
            raise InsuredNotFoundError()

    @classmethod
    def find_all(cls, ):
        insured_da = DataAccess(Insured)
        return insured_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        insured_da = DataAccess(Insured)
        return insured_da.find_by_id(id)


class WorkerService:
    @classmethod
    def save(cls, worker):
        worker_da = DataAccess(Worker)
        worker_da.save(worker)
        return worker

    @classmethod
    def edit(cls, worker):
        worker_da = DataAccess(Worker)
        if worker_da.find_by_id(worker.id):
            worker_da.edit(worker)
            return worker
        else:
            raise WorkerNotFoundError()

    @classmethod
    def remove(cls, id):
        worker_da = DataAccess(Worker)
        if worker_da.find_by_id(id):
            return worker_da.remove(id)
        else:
            raise WorkerNotFoundError()

    @classmethod
    def find_all(cls, ):
        worker_da = DataAccess(Worker)
        return worker_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        worker_da = DataAccess(Worker)
        return worker_da.find_by_id(id)


class MarketerService:
    @classmethod
    def save(cls, marketer):
        marketer_da = DataAccess(Marketer)
        marketer_da.save(marketer)
        return marketer

    @classmethod
    def edit(cls, marketer):
        marketer_da = DataAccess(Marketer)
        if marketer_da.find_by_id(marketer.id):
            marketer_da.edit(marketer)
            return marketer
        else:
            raise MarketerNotFoundError()

    @classmethod
    def remove(cls, id):
        marketer_da = DataAccess(Marketer)
        if marketer_da.find_by_id(id):
            return marketer_da.remove(id)
        else:
            raise MarketerNotFoundError()

    @classmethod
    def find_all(cls, ):
        marketer_da = DataAccess(Marketer)
        return marketer_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        marketer_da = DataAccess(Marketer)
        return marketer_da.find_by_id(id)


class InsuranceSellService:
    @classmethod
    def save(cls, insurance_sell):
        insurance_sell_da = DataAccess(InsuranceSell)
        insurance_sell_da.save(insurance_sell)
        return insurance_sell

    @classmethod
    def edit(cls, insurance_sell):
        insurance_sell_da = DataAccess(InsuranceSell)
        if insurance_sell_da.find_by_id(insurance_sell.id):
            insurance_sell_da.edit(insurance_sell)
            return insurance_sell
        else:
            raise InsuranceSellNotFoundError()

    @classmethod
    def remove(cls, id):
        insurance_sell_da = DataAccess(InsuranceSell)
        if insurance_sell_da.find_by_id(id):
            return insurance_sell_da.remove(id)
        else:
            raise InsuranceSellNotFoundError()

    @classmethod
    def find_all(cls, ):
        insurance_sell_da = DataAccess(InsuranceSell)
        return insurance_sell_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        insurance_sell_da = DataAccess(InsuranceSell)
        return insurance_sell_da.find_by_id(id)


