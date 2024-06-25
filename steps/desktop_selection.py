import tkinter as tk
from tkinter import ttk

class DesktopSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Display detected hardware information
        hardware_label = ttk.Label(self, text="Detected Hardware Information:")
        hardware_label.pack(fill='x', expand=True)

        hardware_info = tk.Text(self, height=10)
        hardware_info.pack(fill='both', expand=True)

        hardware_details = (
            f"CPU Cores: {self.parent.hardware_info['cpu']}\n"
            f"Memory: {self.parent.hardware_info['memory']} GB\n"
            f"CPU Info:\n{self.parent.hardware_info['cpu_info']}\n"
            f"PCI Devices:\n{self.parent.hardware_info['pci_devices']}\n"
            f"Locale:\n{self.parent.hardware_info['locale']}\n"
            f"Keyboard Layout:\n{self.parent.hardware_info['keyboard_layout']}\n"
        )
        hardware_info.insert(tk.END, hardware_details)

        # Desktop environment selection
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
