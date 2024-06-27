import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class FilesystemSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.filesystems = [
            {"name": "BTRFS", "icon": "btrfs.png"},
            {"name": "ZFS", "icon": "zfs.png"},
            {"name": "EXT4", "icon": "ext4.png"},
            {"name": "XFS", "icon": "xfs.png"},
            {"name": "F2FS", "icon": "f2fs.png"}
        ]
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Filesystem:")
        label.pack(fill='x', expand=True)

        self.fs_frame = ttk.Frame(self)
        self.fs_frame.pack(fill='both', expand=True)

        self.fs_icons = {}
        self.selected_fs = tk.StringVar()

        for fs in self.filesystems:
            self.add_filesystem_option(fs["name"], fs["icon"])

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def add_filesystem_option(self, name, icon_path):
        frame = ttk.Frame(self.fs_frame)
        frame.pack(fill='x', expand=True, padx=5, pady=5)

        icon = self.load_icon(icon_path)
        icon_label = ttk.Label(frame, image=icon)
        icon_label.image = icon  # Keep a reference to avoid garbage collection
        icon_label.pack(side='left', padx=5, pady=5)

        label = ttk.Label(frame, text=name)
        label.pack(side='left', padx=5, pady=5)

        radio = ttk.Radiobutton(frame, variable=self.selected_fs, value=name)
        radio.pack(side='right', padx=5, pady=5)

    def load_icon(self, icon_path):
        icon_full_path = os.path.join("icons", icon_path)
        image = Image.open(icon_full_path)
        image = image.resize((32, 32), Image.LANCZOS)  # Updated to use Image.LANCZOS
        return ImageTk.PhotoImage(image)

    def next_step(self):
        selected_fs = self.selected_fs.get()
        print(f"Selected Filesystem: {selected_fs}")
        from steps.swap_file_configuration import SwapFileConfiguration
        self.parent.show_step(SwapFileConfiguration)
