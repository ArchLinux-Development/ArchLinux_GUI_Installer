import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class FilesystemSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.filesystems = [
            {"name": "BTRFS", "icon": "btrfs.png", "description": "Btrfs is a modern file system developed by multiple parties. It is designed to handle the failure of multiple devices gracefully, and includes a number of features that are designed to ensure high data integrity."},
            {"name": "ZFS", "icon": "zfs.png", "description": "ZFS is a combined file system and logical volume manager designed by Sun Microsystems. It provides high storage capacities and integrates volume management, redundancy, and data integrity verification."},
            {"name": "EXT4", "icon": "ext4.png", "description": "Ext4 is the default file system for many Linux distributions. It is a solid, journaled file system that provides a good balance between performance and reliability."},
            {"name": "XFS", "icon": "xfs.png", "description": "XFS is a high-performance 64-bit journaling file system created by Silicon Graphics, Inc (SGI) in 1993. It is particularly proficient at handling large files and at scaling to large file systems."},
            {"name": "F2FS", "icon": "f2fs.png", "description": "F2FS (Flash-Friendly File System) is a file system intended for NAND flash memory-based storage devices. It is designed to take advantage of the characteristics of NAND flash memory."}
        ]
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Filesystem:")
        label.pack(fill='x', expand=True)

        self.fs_frame = ttk.Frame(self)
        self.fs_frame.pack(fill='both', expand=True)

        self.fs_icons = {}
        self.selected_fs = tk.StringVar()
        self.selected_fs.trace('w', self.on_fs_selected)

        for fs in self.filesystems:
            self.add_filesystem_option(fs["name"], fs["icon"], fs["description"])

        self.next_button = ttk.Button(self, text="Next", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(fill='x', expand=True, pady=10)

    def add_filesystem_option(self, name, icon_path, description):
        frame = ttk.Frame(self.fs_frame)
        frame.pack(fill='x', expand=True, padx=5, pady=5)

        icon = self.load_icon(icon_path)
        icon_label = ttk.Label(frame, image=icon)
        icon_label.image = icon  # Keep a reference to avoid garbage collection
        icon_label.pack(side='left', padx=5, pady=5)

        info_frame = ttk.Frame(frame)
        info_frame.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        label = ttk.Label(info_frame, text=name)
        label.pack(anchor='w')

        description_label = ttk.Label(info_frame, text=description, wraplength=400, justify='left')
        description_label.pack(anchor='w')

        radio = ttk.Radiobutton(frame, variable=self.selected_fs, value=name)
        radio.pack(side='right', padx=5, pady=5)

    def load_icon(self, icon_path):
        icon_full_path = os.path.join("icons", icon_path)
        image = Image.open(icon_full_path)
        image = image.resize((32, 32), Image.LANCZOS)  # Updated to use Image.LANCZOS
        return ImageTk.PhotoImage(image)

    def on_fs_selected(self, *args):
        self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        selected_fs = self.selected_fs.get()
        print(f"Selected Filesystem: {selected_fs}")
        from steps.swap_file_configuration import SwapFileConfiguration
        self.parent.show_step(SwapFileConfiguration)
