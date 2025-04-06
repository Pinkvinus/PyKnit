from src.Model.Knitting.Swatches.Swatch import Swatch


class StockinetteSwatch(Swatch):
    def __init__(self, yarnid, gauge, stitches, rows, width, height):
        super().__init__(yarnid, "Stockinette", gauge, stitches, rows, width, height)

    def get_stitches_per_cm(self):
        return super().get_stitches_per_cm()
    
    def get_rows_per_cm(self):
        return super().get_rows_per_cm()
    
    def save(self):
        super().save()
