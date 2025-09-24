
from abc import ABC, abstractmethod
from pathlib import Path

class Swatch(ABC):

    SWATCHES_FILE = Path("../../../Data/Swatches.csv")

    def __init__(self, yarnid:int, pattern:str, gauge:str, stitches:int, rows:int, width:float, height:float):
        if yarnid < 0:
            raise ValueError("Swatch: yarnid has to be a non-negative number")
        if stitches <= 0:
            raise ValueError("Swatch: Stitches has to be a positive number")
        if width <= 0:
            raise ValueError("Swatch: Width has to be a positive number")
        if rows <= 0:
            raise ValueError("Swatch: Rows has to be a positive number")
        if height <= 0:
            raise ValueError("Swatch: Height has to be a positive number")
        
        self.yarnid = yarnid
        self.pattern = pattern
        self.gauge = gauge

        self.st_pr_cm = stitches / width
        self.r_pr_cm = rows / height

    def save(self):
        pass #TODO
