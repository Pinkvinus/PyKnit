from src.Model.Knitting.Patterns.Pattern import Pattern
from src.Model.Knitting.Instructions.CastOnInstruction import CastOnInstruction
from src.Model.Knitting.Instructions.RibbingInstruction import RibbingInstruction
from src.Model.Knitting.Instructions.ShapingInstruction import ShapingInstruction
from src.Model.Knitting.Converters.MeasurementConverter import MeasurementConverter

class CropTop(Pattern):
    def __init__(self, swatch, measurements):
        super().__init__(swatch, measurements)
        self.ribbing = 3
        self.converter = MeasurementConverter(swatch, measurements)
    
    def get_instructions(self):
        waist_stitches = self.converter.get_stitches('waist')

        caston = CastOnInstruction(waist_stitches).get_instructions()

        ribbing_rows = self.converter.get_rows(3)
        ribbing = RibbingInstruction(ribbing_rows, caston[1]).get_instructions()

        underbust = self.converter.get_stitches('underbust')
        waist_to_underbust_rows = self.converter.get_rows('waist to underbust')
        ins = "try to fit the shaping stitches on the same 3rd of the garment"
        shaping_underbust = ShapingInstruction(waist_to_underbust_rows, ribbing[1], underbust, 2, ins)

        



