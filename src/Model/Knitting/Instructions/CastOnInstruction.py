from src.Model.Knitting.Instructions.Instruction import Instruction

class CastOnInstruction(Instruction):
    def __init__(self, stitches):
        super().__init__(1, 0, stitches)

    def get_instructions(self) -> tuple[list[str], int]:
        ins = f"Cast on {self.end_stitches} stitches."
        return ([ins], self.end_stitches)