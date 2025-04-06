import math
from enum import Enum
from src.Model.Knitting.Instructions.Instruction import Instruction

class ShapingType(Enum):
    INCREASE = 1
    DECREASE = 2

class ShapingInstruction(Instruction):
    """
        An instruction covering increase or decrease instructions
    """
    def __init__(self, num_rows, start_stitches, end_stitches, order:int, advanced_instructions):
        super().__init__(num_rows, start_stitches, end_stitches)
        if order < 1:
            raise ValueError("Order can't be less than 1")
        self.order = order
        self.advanced_instructions = advanced_instructions

        if start_stitches < end_stitches:
            self.type = ShapingType.INCREASE
        else:
            self.type = ShapingType.DECREASE


    def __str__(self):
        return super().__str__() + f" Order: {self.order}, Advanced instructions: {self.advanced_instructions}"
    
    def get_instructions(self) -> tuple[list[str], int]:

        instructions = []

        shaping_rows = self.distribute_shaping(self.num_rows, self.start_stitches//self.order, self.end_stitches//self.order)
        rows_as_string = ", ".join(str(x) for x in shaping_rows)

        intro = f"In the next step, we will do some {self.type.name.lower()} shaping"
        overall_steps = f"You should have {self.start_stitches} stiches"
        shaping_steps = f"In the rows {rows_as_string} {self.type.name.lower()} by {self.order}"

        instructions.append(intro)
        instructions.append(overall_steps)
        instructions.append(shaping_steps)

        warning_ins, actual_end_stitches = self.warning_instructions(shaping_rows)



        return instructions + warning_ins, actual_end_stitches
    
    def warning_instructions(self, shaping_rows) -> tuple[list[str], int]:
        actual_end_stitches = 0
        actual_diff = (len(shaping_rows)*self.order)

        if self.type == ShapingType.DECREASE:
            actual_end_stitches = self.start_stitches - actual_diff
        else:
            actual_end_stitches = self.start_stitches + actual_diff
        
        if actual_end_stitches == self.end_stitches:
            return [], actual_end_stitches

        divergence = actual_end_stitches - self.end_stitches
        div_word = ""
        if divergence > 0:
            div_word = "bigger"
        else:
            div_word = "smaller"

        warning1 = f"Note, it was not possible to create perfect {self.type.name.lower()}s"
        warning2 = f"The actual garment is {abs(self.end_stitches - actual_end_stitches)} stitch(es) {div_word} than expected"
        warning3 = f"You should end up with {actual_end_stitches} stitches"

        return [[warning1, warning2, warning3], actual_end_stitches]


    def distribute_shaping(self, num_rows:int, start_stitches:int, end_stitches:int) -> list[int]:
        """
            Distributes shaping stiches over a number of rows.
            Note that if there are more shaping stitches than there are rows
                this function is not suitable.
        """

        total_difference = abs(start_stitches - end_stitches)
        if total_difference == 0:
            return [0] * num_rows

        if num_rows < total_difference:
            raise ValueError("Number of rows need to be greater than total difference")

        extra_stitches = num_rows % total_difference

        # we'll see how many rows per increase are done normally
        normal_shaping = math.floor(num_rows / total_difference)

        previous_index = 0
        shaping_rows = []

        # Populate the array with the rownumbers in reverse spacial order
        while previous_index < num_rows:
            index = normal_shaping + previous_index
            if extra_stitches > 0:
                index = index + 1
                extra_stitches = extra_stitches - 1

            previous_index = index
            shaping_rows.append(index)
        

        # Reversing the spacing in the array
        previous_row = 0
        shaping_rev = [0] * len(shaping_rows)

        for i, rn in enumerate(shaping_rows):
            if previous_row == 0:
                new_rn = (num_rows - rn) + (shaping_rows[1] - shaping_rows[0])
                previous_row = rn
                shaping_rev[i] = new_rn
                continue

            new_rn = (num_rows - rn) + (rn - previous_row)
            previous_row = rn
            shaping_rev[i] = new_rn
        
        shaping_rev.reverse()

        return shaping_rev