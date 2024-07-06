class InsuranceNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Insurance Not Found !!!")