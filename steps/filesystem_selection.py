import tkinter as tk
from tkinter import ttk

class FilesystemSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Filesystem:")
        label.pack(fill='x', expand=True)

        self.filesystems = ["BTRFS", "ZFS", "EXT4", "XFS", "F2FS"]
        self.fs_var = tk.StringVar(value=self.filesystems)
        self.fs_listbox = tk.Listbox(self, listvariable=self.fs_var, selectmode='single')
        self.fs_listbox.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_fs = self.fs_listbox.get(self.fs_listbox.curselection())
        print(f"Selected Filesystem: {selected_fs}")
        from steps.swap_file_configuration import SwapFileConfiguration
        self.parent.show_step(SwapFileConfiguration)
