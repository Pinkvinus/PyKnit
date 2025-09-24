import sys
import os

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

from src.Model.Knitting.Garment.Pattern import Pattern
from src.Model.Knitting.Instructions.CastOn.CastOnInstruction import CastOnInstruction
from src.Model.Knitting.Swatches.Swatch import Swatch

class CropTop(Pattern):
    def __init__(self, swatch, measurements, ease):
        super().__init__(swatch, measurements, ease)
        self.ribbing = 1.5
    
    def get_instructions(self):


        neck_stitches = self.swatch.measurement_to_st(self.measurements['neck circumference'])
        caston = CastOnInstruction(neck_stitches).get_instructions()

        print(caston)



ease = 0.75

measurement = {
    "waist" : 80.5*ease,
    "underbust" : 84*ease,
    "bust": 95*ease,
    "overbust" : 95*ease,
    "waist to underbust" : 16,
    "underbust to bust" : 7,
    "waist to bust" :20 - 1.5,
    "bust to overbust" : 7,
    "bicep" : 35*ease,
    "armscye circumference" : 119*ease,
    "bust to neck" : 18,
    "neck circumference" :60
}

#This swatch has a stretch of 150%
swatch = Swatch(7, 'Stockinette', "5 mm", 31, 36, 19, 14)


ct = CropTop(swatch=swatch, measurements=measurement, ease=5.0).get_instructions()

