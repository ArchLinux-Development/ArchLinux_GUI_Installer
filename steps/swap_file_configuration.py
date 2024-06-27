import tkinter as tk
from tkinter import ttk
import psutil

class SwapFileConfiguration(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Swap File Configuration:")
        label.pack(fill='x', expand=True, padx=10, pady=10)

        self.memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB

        # Default swap size calculations
        self.swap_size = self.calculate_swap_size()
        self.zram_size_options = {
            "1/2 of RAM": self.memory / 2,
            "1x RAM": self.memory,
            "2x RAM": self.memory * 2
        }

        ttk.Label(self, text=f"Detected System Memory: {self.memory:.2f} GB").pack(fill='x', expand=True, padx=10)

        ttk.Label(self, text="Swap File Size (GB):").pack(fill='x', expand=True, padx=10)
        self.swap_size_var = tk.DoubleVar(value=self.swap_size)
        self.swap_size_entry = ttk.Entry(self, textvariable=self.swap_size_var)
        self.swap_size_entry.pack(fill='x', expand=True, padx=10, pady=5)

        self.use_zram_var = tk.BooleanVar()
        self.zram_check = ttk.Checkbutton(self, text="Use ZRAM", variable=self.use_zram_var, command=self.toggle_zram_options)
        self.zram_check.pack(fill='x', expand=True, padx=10, pady=5)

        self.zram_size_var = tk.DoubleVar(value=self.zram_size_options["1/2 of RAM"])
        self.zram_size_label = ttk.Label(self, text="ZRAM Size (GB):")
        self.zram_size_combobox = ttk.Combobox(self, values=list(self.zram_size_options.keys()), state='readonly')
        self.zram_size_combobox.bind("<<ComboboxSelected>>", self.update_zram_size)
        self.zram_size_entry = ttk.Entry(self, textvariable=self.zram_size_var)

        # Initially hide ZRAM options
        self.zram_size_label.pack_forget()
        self.zram_size_combobox.pack_forget()
        self.zram_size_entry.pack_forget()

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True, padx=10, pady=10)

    def calculate_swap_size(self):
        if self.memory < 2:
            return self.memory * 2
        elif self.memory < 8:
            return self.memory
        else:
            return self.memory / 2

    def toggle_zram_options(self):
        if self.use_zram_var.get():
            self.zram_size_label.pack(fill='x', expand=True, padx=10, pady=5)
            self.zram_size_combobox.pack(fill='x', expand=True, padx=10, pady=5)
            self.zram_size_entry.pack(fill='x', expand=True, padx=10, pady=5)
        else:
            self.zram_size_label.pack_forget()
            self.zram_size_combobox.pack_forget()
            self.zram_size_entry.pack_forget()

    def update_zram_size(self, event):
        selected_option = self.zram_size_combobox.get()
        self.zram_size_var.set(self.zram_size_options[selected_option])

    def next_step(self):
        swap_size = self.swap_size_var.get()
        use_zram = self.use_zram_var.get()
        zram_size = self.zram_size_var.get() if use_zram else None
        print(f"Swap Size: {swap_size} GB, Use ZRAM: {use_zram}, ZRAM Size: {zram_size} GB")

        from steps.bootloader_selection import BootloaderSelection
        self.parent.show_step(BootloaderSelection)
