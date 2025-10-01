from pathlib import Path

DATA_FOLDER = Path("../../../Data")

class Garment:

    def __init__(self, name:str, segments=None):
        self.name = name
        self.segments = []
        if segments is not None:
            self.parts = segments
        
        
