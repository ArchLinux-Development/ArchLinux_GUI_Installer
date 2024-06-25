import tkinter as tk
from tkinter import ttk
from steps.desktop_selection import DesktopSelection

class ArchLinuxInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arch Linux GUI Installer")
        self.geometry("800x600")
        self.current_step = None
        self.show_step(DesktopSelection)

    def show_step(self, step_class):
        if self.current_step:
            self.current_step.destroy()
        self.current_step = step_class(self)
        self.current_step.pack(fill='both', expand=True)

if __name__ == "__main__":
    app = ArchLinuxInstaller()
    app.mainloop()
