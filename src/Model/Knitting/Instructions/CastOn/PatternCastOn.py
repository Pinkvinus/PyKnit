from src.Model.Knitting.Instructions.CastOn.CastOnInstruction import CastOnInstruction
from src.Model.Knitting.Instructions.RibbingInstruction import RibbingInstruction

class PatternOnInstruction(CastOnInstruction, RibbingInstruction):
    def __init__(self, stitches):
        super().__init__(1, 0, stitches)

    def get_instructions(self) -> tuple[list[str], int]:


        if self.start_stitches % len(self.pattern) != 0:
            self.start_stitches = self.nearest_multiple(self.start_stitches, len(self.pattern))
        
        

        

        ins = f"Cast on {self.end_stitches} stitches."
        return ([ins], self.end_stitches)