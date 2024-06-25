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
        selected_bootloader_indices = self.bootloader_listbox.curselection()
        if not selected_bootloader_indices:
            print("No bootloader selected")
            return
        selected_bootloader = self.bootloaders[selected_bootloader_indices[0]]
        print(f"Selected Bootloader: {selected_bootloader}")
        from steps.swap_file_configuration import SwapFileConfiguration
        self.parent.show_step(SwapFileConfiguration)
