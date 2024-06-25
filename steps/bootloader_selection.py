import tkinter as tk
from tkinter import ttk

class BootloaderSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Bootloader:")
        label.pack(fill='x', expand=True)

        self.bootloaders = ["GRUB", "systemd-boot", "rEFInd", "LILO"]
        self.bootloader_var = tk.StringVar(value=self.bootloaders)
        self.bootloader_listbox = tk.Listbox(self, listvariable=self.bootloader_var, selectmode='single')
        self.bootloader_listbox.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_bootloader = self.bootloader_listbox.get(self.bootloader_listbox.curselection())
        print(f"Selected Bootloader: {selected_bootloader}")
        # Here you would transition to the next step, e.g., swap file configuration
