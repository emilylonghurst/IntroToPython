
from account_basis import Account


class Isa(Account):

    def __init__(self, isa_name, isa_number, isa_pin, isa_interest):
        super().__init__(isa_name, isa_number, isa_pin)
        self._interest = isa_interest
