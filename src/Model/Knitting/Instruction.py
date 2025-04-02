from abc import ABC, abstractmethod

class Instruction(ABC):
    num_rows = 0
    start_stitches = 0
    end_stitches = 0

    def __init__(self, num_rows:int, start_stitches:int, end_stitches:int):
        """
            Params:
                num_rows       - The change in number of rows for the section
                start_stitches - The number of stitches at the start of the section
                end_stitches   - The number of stitches at the end of the section 
                order          - When an increase or decrease happens 
        """

        if num_rows < 0 or start_stitches < 0 or end_stitches < 0 :
            raise ValueError("Instruction can't be initialised with negative values")

        self.num_rows = num_rows
        self.start_stitches = start_stitches
        self.end_stitches = end_stitches
    
    def __str__(self) -> str:
        return f"Number of rows: {self.num_rows}, initial number of stitches: {self.start_stitches}, Terminal number of stitches: {self.end_stitches}"

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def get_instructions(self) -> list[str]:
        pass


class ShapingInstruction(Instruction):
    """
        An instruction covering increase or decrease instructions
    """
    order = 1
    advanced_instructions = ""

    def __init__(self, num_rows, start_stitches, end_stitches, order:int, advanced_instructions):
        super().__init__(num_rows, start_stitches, end_stitches)
        self.order = order
        self.advanced_instructions = advanced_instructions

    def __str__(self):
        return super().__str__() + f" Order: {self.order}, Advanced instructions: {self.advanced_instructions}"
    
    def print(self):
        ...
    
    def get_instructions(self) -> list[str]:
        ...