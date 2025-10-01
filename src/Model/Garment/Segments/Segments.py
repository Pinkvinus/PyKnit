from abc import ABC, abstractmethod

class Segment(ABC):
    def __init__(self, name, stitches, rows, technique):
        self.name = name
        self.stitches = stitches
        self.rows = rows
        self.technique = technique
        self.next_segment = None
        self.previous_segment = None

    def connect(self, next_segment):
        self.next_segment = next_segment
        next_segment.previous_segment = self

    @abstractmethod
    def instructions(self):
        """Return knitting instructions for this segment"""
        pass