import tkinter as tk


class ShapeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Back button
        tk.Button(self, text="Back", command=lambda: controller.show_frame(ProfileSelectView)).pack(pady=5)

        # Canvas with shapes
        canvas = tk.Canvas(self, width=400, height=300, bg="white")
        canvas.pack(pady=10)

        canvas.create_rectangle(50, 50, 150, 150, fill="lightblue", outline="black")
        canvas.create_oval(200, 50, 300, 150, fill="pink", outline="red")
        canvas.create_line(50, 200, 300, 200, width=3, fill="green")
        canvas.create_polygon(100, 250, 200, 200, 300, 250, 200, 300, fill="orange")
