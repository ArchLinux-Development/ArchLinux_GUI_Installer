import tkinter as tk
from tkinter import ttk

class SwapFileConfiguration(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Swap File Configuration:")
        label.pack(fill='x', expand=True)

        ttk.Label(self, text="Swap File Size (MB):").pack(fill='x', expand=True)
        self.swap_size_entry = ttk.Entry(self)
        self.swap_size_entry.pack(fill='x', expand=True)

        self.zram_var = tk.BooleanVar()
        self.zram_check = ttk.Checkbutton(self, text="Enable Zram Swap", variable=self.zram_var)
        self.zram_check.pack(fill='x', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        swap_size = self.swap_size_entry.get()
        enable_zram = self.zram_var.get()
        print(f"Swap File Size: {swap_size} MB, Zram: {enable_zram}")
        from steps.additional_software import AdditionalSoftware
        self.parent.show_step(AdditionalSoftware)
