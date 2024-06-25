import tkinter as tk
from tkinter import ttk
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
            info['cpu_info'] = self.extract_cpu_model(result.stdout)
        except Exception as e:
            info['cpu_info'] = str(e)

        try:
            result = subprocess.run(['lspci'], capture_output=True, text=True)
            info['gpu_info'] = self.extract_gpu_model(result.stdout)
        except Exception as e:
            info['gpu_info'] = str(e)

        try:
            result = subprocess.run(['locale'], capture_output=True, text=True)
            info['locale'] = result.stdout.strip()
        except Exception as e:
            info['locale'] = str(e)

        try:
            result = subprocess.run(['localectl', 'status'], capture_output=True, text=True)
            info['keyboard_layout'] = self.extract_keyboard_layout(result.stdout)
        except Exception as e:
            info['keyboard_layout'] = str(e)

        try:
            result = subprocess.run(['dmidecode', '-s', 'system-product-name'], capture_output=True, text=True)
            info['virtualization'] = self.detect_virtualization(result.stdout)
        except Exception as e:
            info['virtualization'] = str(e)

        return info

    def extract_cpu_model(self, lscpu_output):
        for line in lscpu_output.split('\n'):
            if 'Model name' in line:
                return line.split(':')[1].strip()
        return "Unknown CPU"

    def extract_gpu_model(self, lspci_output):
        for line in lspci_output.split('\n'):
            if 'VGA compatible controller' in line:
                return line.split(':')[2].strip()
        return "Unknown GPU"

    def extract_keyboard_layout(self, localectl_output):
        for line in localectl_output.split('\n'):
            if 'Layout' in line:
                return line.split(':')[1].strip()
        return "Unknown Layout"

    def detect_virtualization(self, dmidecode_output):
        if 'VirtualBox' in dmidecode_output:
            return 'VirtualBox'
        else:
            return 'Physical Machine'

if __name__ == "__main__":
    from steps.desktop_selection import DesktopSelection
    app = ArchLinuxInstaller()
    app.mainloop()
