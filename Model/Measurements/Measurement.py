import pandas as pd


DATA_FOLDER = "../Data"
MEASUREMENT_DESCRIPTION_DF = pd.read_csv( DATA_FOLDER + "/MeasurementDescriptions.csv")


class Measurement:

    def __init__(self, name:str, measurement:int):

        

        self.name = name
        self.name = measurement
    
    def __str__(self):
        return f"{self.name}: {self.measurement}"

