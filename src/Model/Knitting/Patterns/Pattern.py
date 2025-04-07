from abc import ABC, abstractmethod
from src.Model.Measurements.Measurement import Measurement
from src.Model.Knitting.Swatches.Swatch import Swatch

class Pattern(ABC): 
    # An abstract class for a knitting pattern

    def __init__(self, swatch:Swatch, measurements:list[Measurement]):
        self.swatch = swatch
        self.measurements = measurements

    @abstractmethod
    def get_instructions() -> list[str]:
        """
            Returns

                - list[str] : A list of the several steps needed to create a garment
        """
        pass
