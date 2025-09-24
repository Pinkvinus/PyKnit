import tkinter as tk
from src.View.ProfileViews.ProfileDetailView import ProfileDetailView
from src.View.ProfileViews.CreateProfileView import CreateProfileView

class ProfileSelectView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Choose a profile:").pack(pady=10)

        profiles = ["Alice", "Bob", "Charlie"]
        for profile in profiles:
            tk.Button(
                self, text=profile,
                command=lambda p=profile: self.open_profile(p)
            ).pack(pady=5)
        
        tk.Button(self, text="Create New Profile", command=self.create_profile).pack(pady=10)

    def open_profile(self, name):
        # Pass data to the detail view
        detail_view = self.controller.frames[ProfileDetailView]
        detail_view.set_profile(name)
        self.controller.show_frame(ProfileDetailView)
    
    def create_profile(self):
        create_view = self.controller.frames[CreateProfileView]
        self.controller.show_frame(CreateProfileView)
