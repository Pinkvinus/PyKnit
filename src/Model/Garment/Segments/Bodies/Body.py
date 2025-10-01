from src.Model.Garment.Segments.Segments import Segment

class Body(Segment):
    def __init__(self, name, stitches, rows, technique):
        super().__init__(name, stitches, rows, technique)
        self.left_sleeve = None
        self.right_sleeve = None
        


    def instructions(self):
        return (f"{self.name}: Cast on {self.stitches} stitches, "
                f"work {self.rows} rows in {self.technique.name}. "
                f"Work in the round until desired length.")
