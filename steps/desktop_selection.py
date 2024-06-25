import tkinter as tk
from tkinter import ttk

class DesktopSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Desktop Environment:")
        label.pack(fill='x', expand=True)

        self.desktop_env = ttk.Combobox(self, values=["GNOME", "KDE Plasma", "XFCE", "Cinnamon", "MATE", "LXQt", "Budgie", "i3", "Deepin"])
        self.desktop_env.pack(fill='x', expand=True)
        self.desktop_env.current(0)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_desktop = self.desktop_env.get()
        print(f"Selected Desktop Environment: {selected_desktop}")
        from steps.software_selection import SoftwareSelection
        self.parent.show_step(SoftwareSelection)
