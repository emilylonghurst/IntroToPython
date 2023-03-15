
from isa import Isa


class Lisa(Isa):

    def __init__(self, lisa_name, lisa_number, lisa_pin, lisa_interest, lisa_modifier):
        super().__init__(lisa_name, lisa_number, lisa_pin, lisa_interest)
        self._modifier = lisa_modifier
