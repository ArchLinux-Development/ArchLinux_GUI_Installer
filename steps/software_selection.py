import tkinter as tk
from tkinter import ttk

class SoftwareSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Software Options:")
        label.pack(fill='x', expand=True)

        self.software_options = ["Minimal", "Normal", "Maximal"]
        self.software_var = tk.StringVar(value=self.software_options)
        self.software_listbox = tk.Listbox(self, listvariable=self.software_var, selectmode='single')
        self.software_listbox.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_software_indices = self.software_listbox.curselection()
        if not selected_software_indices:
            print("No software option selected")
            return
        selected_software = self.software_options[selected_software_indices[0]]
        print(f"Selected Software: {selected_software}")
        from steps.filesystem_selection import FilesystemSelection
        self.parent.show_step(FilesystemSelection)
