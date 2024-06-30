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

        frame = ttk.Frame(self)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        ttk.Label(frame, text=f"Detected System Memory: {self.memory:.2f} GB").grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        ttk.Label(frame, text="Swap File Size (GB):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.swap_size_var = tk.DoubleVar(value=self.swap_size)
        self.swap_size_entry = ttk.Entry(frame, textvariable=self.swap_size_var)
        self.swap_size_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.use_zram_var = tk.BooleanVar()
        self.zram_check = ttk.Checkbutton(frame, text="Use ZRAM", variable=self.use_zram_var, command=self.toggle_zram_options)
        self.zram_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.zram_size_label = ttk.Label(frame, text="ZRAM Size:")
        self.zram_size_var = tk.DoubleVar(value=self.zram_size_options["1/2 of RAM"])  # Initialize zram_size_var
        self.zram_size_combobox = ttk.Combobox(frame, values=list(self.zram_size_options.keys()), state='readonly')
        self.zram_size_combobox.current(0)  # Set default selection
        self.zram_size_combobox.bind("<<ComboboxSelected>>", self.update_zram_size)

        # Initially hide ZRAM options
        self.zram_size_label.grid_forget()
        self.zram_size_combobox.grid_forget()

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
            self.zram_size_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
            self.zram_size_combobox.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        else:
            self.zram_size_label.grid_forget()
            self.zram_size_combobox.grid_forget()

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

