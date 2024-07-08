from insurance.controller.exception.insurance_exception import InsuranceNotFoundError, InsuredNotFoundError, \
    WorkerNotFoundError
from insurance.model.da.insurance_da import DataAccess
from insurance.model.entity.marketer import Marketer
from insurance.model.entity.worker import Worker
from insurance.model.entity.__init__ import *
from insurance.model.entity.insured import Insured


class InsuranceService:
    @classmethod
    def save(cls, insurance):
        insurance_da = DataAccess(Insurance)
        insurance_da.save(insurance)
        return insurance

    @classmethod
    def edit(cls, insurance):
        insurance_da = DataAccess(Insurance)
        if insurance_da.find_by_id(insurance.id):
            insurance_da.edit(insurance)
            return insurance
        else:
            raise InsuranceNotFoundError()

    @classmethod
    def remove(cls, id):
        insurance_da = DataAccess(Insurance)
        if insurance_da.find_by_id(id):
            return insurance_da.remove(id)
        else:
            raise InsuranceNotFoundError()

    @classmethod
    def find_all(cls, ):
        insurance_da = DataAccess(Insurance)
        return insurance_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        insurance_da = DataAccess(Insurance)
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
