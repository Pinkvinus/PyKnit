from abc import ABC, abstractmethod

class Instruction(ABC):

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
    def get_instructions(self) -> tuple[list[str], int]:
        """
            This method should return a tuple of a list of strings and an integer
            containing the information on how to perform the instructions

            Returns:
            
                - list[str] : A list of textual instructions
                - ins       : The actual number of stitches at the end
        """
        pass







        



