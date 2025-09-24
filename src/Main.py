import tkinter as tk
from src.View.ProfileViews.ProfileSelectView import ProfileSelectView
from src.View.ProfileViews.ProfileDetailView import ProfileDetailView
from src.View.ProfileViews.CreateProfileView import CreateProfileView  # Add this import


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyKnit")
        self.geometry("300x200")

        # Container for views
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Initialize two views
        for F in (ProfileSelectView, ProfileDetailView, CreateProfileView):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ProfileSelectView)

    def show_frame(self, view_class):
        frame = self.frames[view_class]
        frame.tkraise()  # Bring to front



if __name__ == "__main__":
    app = App()
    app.mainloop()