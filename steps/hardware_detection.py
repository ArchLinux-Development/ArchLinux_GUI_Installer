import tkinter as tk
from tkinter import ttk

class HardwareDetection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
        self.detect_hardware()

    def create_widgets(self):
        label = ttk.Label(self, text="Hardware Detection:")
        label.pack(fill='x', expand=True)

        self.hardware_info = tk.Text(self, height=15)
        self.hardware_info.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def detect_hardware(self):
        # Simulate hardware detection
        hardware_data = "Detected Hardware:\n"
        hardware_data += "CPU: Intel Core i7\n"
        hardware_data += "GPU: NVIDIA GTX 1080\n"
        hardware_data += "Memory: 16GB\n"
        hardware_data += "Locale: en_US.UTF-8\n"
        hardware_data += "Keyboard Layout: US"
        self.hardware_info.insert(tk.END, hardware_data)

    def next_step(self):
        from steps.bootloader_selection import BootloaderSelection
        self.parent.show_step(BootloaderSelection)
