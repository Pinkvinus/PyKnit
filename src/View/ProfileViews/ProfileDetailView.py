import tkinter as tk

class ProfileDetailView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Profile details here")
        self.label.pack(pady=20)

        from src.View.ProfileViews.ProfileSelectView import ProfileSelectView  # Moved import here

        tk.Button(
            self, text="Back",
            command=lambda: controller.show_frame(ProfileSelectView)
        ).pack()

    def set_profile(self, name):
        self.label.config(text=f"Welcome, {name}!")