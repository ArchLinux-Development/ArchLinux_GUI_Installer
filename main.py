import tkinter as tk
from tkinter import ttk
from steps.desktop_selection import DesktopSelection
import psutil
import subprocess

class ArchLinuxInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arch Linux GUI Installer")
        self.geometry("800x600")
        self.current_step = None
        self.hardware_info = self.detect_hardware()
        self.show_step(DesktopSelection)

    def show_step(self, step_class):
        if self.current_step:
            self.current_step.destroy()
        self.current_step = step_class(self)
        self.current_step.pack(fill='both', expand=True)

    def detect_hardware(self):
        info = {}
        info['cpu'] = psutil.cpu_count(logical=True)
        info['memory'] = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert bytes to GB

        try:
            result = subprocess.run(['lscpu'], capture_output=True, text=True)
            info['cpu_info'] = result.stdout
        except Exception as e:
            info['cpu_info'] = str(e)

        try:
            result = subprocess.run(['lspci', '-nnk'], capture_output=True, text=True)
            info['pci_devices'] = result.stdout
        except Exception as e:
            info['pci_devices'] = str(e)

        try:
            result = subprocess.run(['locale'], capture_output=True, text=True)
            info['locale'] = result.stdout
        except Exception as e:
            info['locale'] = str(e)

        try:
            result = subprocess.run(['localectl', 'status'], capture_output=True, text=True)
            info['keyboard_layout'] = result.stdout
        except Exception as e:
            info['keyboard_layout'] = str(e)

        return info

if __name__ == "__main__":
    app = ArchLinuxInstaller()
    app.mainloop()
