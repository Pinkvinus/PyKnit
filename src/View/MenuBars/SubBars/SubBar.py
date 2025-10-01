import tkinter as tk
from tkinter import ttk


# -------- Subbar base and variants --------
class SubBar(ttk.Frame):
    """Base class for interchangeable sub toolbars."""
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style="Subbar.TFrame")


class SubBarA(SubBar):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Draw Rectangle",
                   command=lambda: parent.master.draw("rect")).pack(side="left", padx=2)
        ttk.Button(self, text="Clear", command=parent.master.clear_canvas).pack(side="left", padx=2)


class SubBarB(SubBar):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Draw Oval",
                   command=lambda: parent.master.draw("oval")).pack(side="left", padx=2)
        ttk.Button(self, text="Clear", command=parent.master.clear_canvas).pack(side="left", padx=2)

