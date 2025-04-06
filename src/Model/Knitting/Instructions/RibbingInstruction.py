import sys
import os

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path


from src.Model.Knitting.Instructions.Instruction import Instruction

class RibbingInstruction(Instruction):
    """
        An instruction covering a simple ribbing instruction
    """

    ALLOWED_PATTERN_CHAR = {'x', 'o'}


    def __init__(self, num_rows, stitches, pattern='xo'):
        super().__init__(num_rows, stitches, stitches)

        if not set(pattern.lower()) <= self.ALLOWED_PATTERN_CHAR:
            raise ValueError("RibbingInstruction: init - Pattern contains unallowed chars")

        self.pattern = pattern

    def get_instructions(self) -> tuple[list[str], int]:

        # Check whether the pattern will lign up with the number of stitches
        instructions = []
        new_end_stitches = self.end_stitches

        if self.start_stitches % len(self.pattern) != 0:

            new_end_stitches = self.nearest_multiple(self.start_stitches, len(self.pattern))

            warning1 = f"Note that the wanted number of stitches({self.start_stitches}) does not align with the pattern."
            warning2 = f"we found that {new_end_stitches} is the nearest multiple."

            instructions = [warning1, warning2]

            if abs(new_end_stitches - self.end_stitches) > 10:
                warning3 = f"Note that this change is more than 10 stitches. This may affect the final product."
                instructions.append(warning3)

            warning4 = f"We recommend that you cast on this number of stitches instead."
            instructions.append(warning4)

        ins1 = f"Knit in a [{self.pattern}] ribbing pattern for {self.num_rows} rows."

        instructions.append(ins1)

        return instructions, new_end_stitches
    
    def nearest_multiple(self, A, B):
        lower = (A // B) * B
        upper = lower + B
        # Return the one closer to A
        if abs(A - lower) <= abs(A - upper):
            return lower
        return upper
        

r = RibbingInstruction(20, 157)

print(r.get_instructions())




