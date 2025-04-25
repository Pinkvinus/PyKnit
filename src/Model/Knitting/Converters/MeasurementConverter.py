from src.Model.Measurements.Measurement import Measurement
from src.Model.Knitting.Swatches.Swatch import Swatch

class MeasurementConverter():
    def __init__(self, swatch:Swatch, measurement:Measurement):
        self.stitches_per_cm = swatch.get_stitches_per_cm()
        self.rows_pr_cm = swatch.get_rows_per_cm()
        self.measurement = measurement
    
    def get_stitches(self, m:str) -> int:
        """
            Converts a measurement into a number of stitches

            params:

                - m : measurement
            
            returns:

                - The number of stitches that will create the same dimensions
        """
        return round(self.stitches_per_cm * self.measurement[m])
    
    def get_rows(self, m:str) -> int:
        """
            Converts a measurement into a number of rows

            params:

                - m : measurement

            returns:
                - The number of rows that will create the same dimensions
        """
        return round(self.rows_pr_cm * self.measurement[m])
    
    def measurement_to_rows(self, m:int | float) -> int :
        return round(self.rows_pr_cm * m)
    
    def measurement_to_stitches(self, m:int | float) -> int:
        return round(self.stitches_per_cm * m)