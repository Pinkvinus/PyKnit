
from abc import ABC, abstractmethod
import csv
from pathlib import Path

class Swatch(ABC):

    SWATCHES_FILE = Path("../../../Data/Swatches.csv")

    def __init__(self, yarnid:int, pattern_type:str, gauge:str, stitches:int, rows:int, width:float, height:float):
        if yarnid < 0:
            raise ValueError("Swatch: yarnid has to be a non-negative number")
        self.yarnid = yarnid

        self.pattern_type = pattern_type
        self.gauge = gauge

        if stitches <= 0:
            raise ValueError("Swatch: Stitches has to be a positive number")
        self.stitches = stitches

        if rows <= 0:
            raise ValueError("Swatch: Rows has to be a positive number")
        self.rows = rows

        if width <= 0:
            raise ValueError("Swatch: Width has to be a positive number")
        self.width = width

        if height <= 0:
            raise ValueError("Swatch: Height has to be a positive number")
        self.height = height
    
    def get_stitches_per_cm(self):
        return self.stitches // self.width
    
    def get_rows_per_cm(self):
        return self.rows // self.height
    
    def save(self):
        with open(self.SWATCHES_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)

            swatch = [self.yarnid,
                      self.pattern_type,
                      '',
                      self.gauge,
                      self.stitches,
                      self.rows,
                      self.width,
                      self.height]
            
            writer.writerow(swatch)

        print('Saved')
