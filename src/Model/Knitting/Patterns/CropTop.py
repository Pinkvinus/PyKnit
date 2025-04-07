from src.Model.Knitting.Patterns.Pattern import Pattern
from src.Model.Knitting.Instructions.CastOnInstruction import CastOnInstruction
from src.Model.Knitting.Instructions.RibbingInstruction import RibbingInstruction
from src.Model.Knitting.Instructions.ShapingInstruction import ShapingInstruction

class CropTop(Pattern):
    def __init__(self, swatch, measurements):
        super().__init__(swatch, measurements)
        self.ribbing = 3
    
    def get_instructions(self):
        waist = self.measurements["waist"]
        waist_stitches = waist * self.swatch.get_stitches_per_cm

        caston = CastOnInstruction(waist_stitches).get_instructions()

        ribbing_rows = self.swatch.get_rows_per_cm() * self.ribbing
        ribbing = RibbingInstruction(ribbing_rows, caston[1]).get_instructions()

        underbust = 
        waist_to_underbust = self.measurements["waist to underbust"]
        waist_to_underbust_rows = self.swatch.get_rows_per_cm() * waist_to_underbust
        shaping_underbust = ShapingInstruction()



