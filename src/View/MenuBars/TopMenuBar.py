import tkinter as tk

class TopMenuBar(tk.Menu):
    
    def __init__(self, parent):
        super().__init__(parent)

        self.add_file_menu()
        self.add_view_menu()
        self.add_segment_menu()


    def add_file_menu(self):
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New Project", command=lambda: print("New Project")) #TODO
        file_menu.add_command(label="Save Project", command=lambda: print("Save Project")) #TODO
        file_menu.add_command(label="Load Project", command=lambda: print("Load File")) #TODO
        file_menu.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="File", menu=file_menu)

    def add_segment_menu(self):
        segment_menu = tk.Menu(self, tearoff=0)
        segment_menu.add_command(label="Remove Segment", command=lambda: print("Remove Segment")) #TODO
        self.add_cascade(label="Segment", menu=segment_menu)

    def add_view_menu(self):
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label="View 1", command=lambda: self.show_frame(View1))
        view_menu.add_command(label="View 2", command=lambda: self.show_frame(View2))
        self.add_cascade(label="View", menu=view_menu)