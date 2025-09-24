from pathlib import Path

DATA_FOLDER = Path("../../../Data")

class Garment:

    def __init__(self, name:str):
        self.name = name
        self.measurements = {}

    def __str__(self):
        return f"{self.name}: {self.value}{self.unit}"
