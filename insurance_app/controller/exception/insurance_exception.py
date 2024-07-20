class InsuranceNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Insurance Not Found !!!")


class InsuredNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Insured Not Found !!!")


class WorkerNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Worker Not Found !!!")


class MarketerNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Marketer Not Found !!!")


class InsuranceSellNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Insurance Sell Not Found !!!")
