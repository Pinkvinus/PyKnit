import sys
import os

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

from src.Model.Knitting.Patterns.Pattern import Pattern
from src.Model.Knitting.Instructions.CastOnInstruction import CastOnInstruction
from src.Model.Knitting.Instructions.RibbingInstruction import RibbingInstruction
from src.Model.Knitting.Instructions.ShapingInstruction import ShapingInstruction
from src.Model.Knitting.Converters.MeasurementConverter import MeasurementConverter
from src.Model.Knitting.Swatches.StockinetteSwatch import StockinetteSwatch

class CropTop(Pattern):
    def __init__(self, swatch, measurements, ease):
        super().__init__(swatch, measurements, ease)
        self.ribbing = 1.5
    
    def get_instructions(self):

        converter = MeasurementConverter(self.swatch, self.measurements)

        waist_stitches = converter.get_stitches('waist')

        caston = CastOnInstruction(waist_stitches).get_instructions()

        ribbing_rows = converter.measurement_to_rows(self.ribbing)
        ribbing = RibbingInstruction(ribbing_rows, caston[1]).get_instructions()


        ins1 = "Now it's time for the shaping of the bust"
        waist_to_bust = converter.get_rows('waist to bust')
        ins2 = "try to fit the shaping stitches on the same 3rd of the garment"
        bust = converter.get_stitches('bust')
        shaping_bust = ShapingInstruction(waist_to_bust, ribbing[1], bust, 2, '').get_instructions()

        bust_to_overbust = converter.get_rows("bust to overbust")
        overbust = converter.get_stitches('overbust')
        shaping_overbust = ShapingInstruction(bust_to_overbust, shaping_bust[1], overbust, 2, '').get_instructions()


        return [caston, ins1, ribbing, shaping_bust, shaping_overbust]



ease = 0.75

measurement = {
    "waist" : 80.5*ease,
    "underbust" : 84*ease,
    "bust": 95*ease,
    "overbust" : 95*ease,
    "waist to underbust" : 16,
    "underbust to bust" : 7,
    "waist to bust" :20 - 1.5,
    "bust to overbust" : 7
}

#This swatch has a stretch of 150%
swatch = StockinetteSwatch(7, "5 mm", 31, 36, 19, 14)

ct = CropTop(swatch=swatch, measurements=measurement, ease=5.0)




for i in ct.get_instructions():
    print(i)


