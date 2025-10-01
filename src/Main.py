import tkinter as tk
from tkinter import ttk
from src.View.ProjectViews.ShapeView import ShapeView  # Example additional view
from src.View.MenuBars.TopMenuBar import TopMenuBar  # Import the menu bar


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyKnit")
        self.geometry("300x200")

        # -------- Top menu bar --------
        menubar = TopMenuBar(self)
        self.config(menu=menubar)

        # -------- Toolbar container --------
        self.toolbar_container = tk.Frame(self, height=40, bg="lightgray")
        self.toolbar_container.pack(fill="x", side="top")


        # Container for views
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}


        self.show_frame(ShapeView)

    def show_frame(self, view_class):
        if view_class not in self.frames:
            frame = view_class(self.container, self)  # pass app so views can request toolbar
            self.frames[view_class] = frame
            frame.pack(fill="both", expand=True)

        frame = self.frames[view_class]
        frame.tkraise()
        # Let the view decide what toolbar to use
        if hasattr(frame, "toolbar_class"):
            self.set_toolbar(frame.toolbar_class)
        else:
            self.set_toolbar(None)

    def set_toolbar(self, toolbar_class=None):
        """Swap the toolbar for the given toolbar_class"""
        # Clear old toolbar
        for widget in self.toolbar_container.winfo_children():
            widget.destroy()

        # If toolbar_class is provided, create it
        if toolbar_class:
            toolbar = toolbar_class(self.toolbar_container, self)
            toolbar.pack(fill="x")


if __name__ == "__main__":
    app = App()
    app.mainloop()