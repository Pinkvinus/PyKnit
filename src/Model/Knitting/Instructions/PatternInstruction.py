from src.Model.Knitting.Instructions.Instruction import Instruction

class PatternInstruction(Instruction):
    """
        An instruction covering pattern instructions
    """

    def __init__(self, num_rows, stitches, pattern:str):
        super().__init__(num_rows, stitches, stitches)

        self.pattern = pattern

    def get_instructions(self) -> tuple[list[str], int]:

        # Check whether the pattern will lign up with the number of stitches
        instructions = []

        ins, new_end_stitches = self.check_stitches
        if ins != None:
            instructions = ins
            self.end_stitches = new_end_stitches

        ins1 = f"Knit in a [{self.pattern}] pattern for {self.num_rows} rows."
        instructions.append(ins1)

        return instructions, self.end_stitches
    
    def nearest_multiple(self, A, B):
        lower = (A // B) * B
        upper = lower + B
        # Return the one closer to A
        if abs(A - lower) <= abs(A - upper):
            return lower
        return upper
    
    def check_stitches(self):
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
            return instructions, new_end_stitches
        return None, None