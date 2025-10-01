import tkinter as tk


class ShapeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Back button
        tk.Button(self, text="Back", command=lambda: controller.show_frame(ProfileSelectView)).pack(pady=5)

        # Canvas with shapes
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_rectangle(50, 50, 150, 150, fill="lightblue", outline="black")
        self.canvas.create_oval(200, 50, 300, 150, fill="pink", outline="red")
        self.canvas.create_line(50, 200, 300, 200, width=3, fill="green")
        self.canvas.create_polygon(100, 250, 200, 200, 300, 250, 200, 300, fill="orange")

    def on_resize(self, event):
        """Clear and redraw something to match new size."""
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        self.canvas.create_text(w//2, h//2, text=f"{w} x {h}", font=("Arial", 20))