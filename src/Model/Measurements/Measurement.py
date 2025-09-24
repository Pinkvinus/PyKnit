import pandas as pd
from pathlib import Path
from src.Model.Measurements.MeasurementType import MeasurementType

DATA_FOLDER = Path("../../../Data")
MEASUREMENT_DESCRIPTION_DF = pd.read_csv( DATA_FOLDER.joinpath("MeasurementDescriptions.csv"))


class Measurement:

    def __init__(self, name:str, value:int, unit='cm'):

        self.name = name
        self.value = value
        self.unit = unit
    
    def __str__(self):
        return f"{self.name}: {self.value}{self.unit}"

