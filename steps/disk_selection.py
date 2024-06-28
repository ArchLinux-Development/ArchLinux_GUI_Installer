import tkinter as tk
from tkinter import ttk
import psutil

class DiskSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.disks = self.get_disks()
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Disk:")
        label.pack(fill='x', expand=True, padx=10, pady=10)

        self.disk_frame = ttk.Frame(self)
        self.disk_frame.pack(fill='both', expand=True)

        self.selected_disk = tk.StringVar()
        self.selected_disk.trace('w', self.on_disk_selected)

        for disk in self.disks:
            self.add_disk_option(disk)

        self.next_button = ttk.Button(self, text="Next", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(fill='x', expand=True, padx=10, pady=10)

    def get_disks(self):
        disks = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "total": usage.total / (1024 ** 3),
                "used": usage.used / (1024 ** 3),
                "free": usage.free / (1024 ** 3),
            })
        return disks

    def add_disk_option(self, disk):
        frame = ttk.Frame(self.disk_frame)
        frame.pack(fill='x', expand=True, padx=5, pady=5)

        disk_info = f"{disk['device']} ({disk['mountpoint']}) - {disk['fstype']} - Total: {disk['total']:.2f} GB, Used: {disk['used']:.2f} GB, Free: {disk['free']:.2f} GB"
        label = ttk.Label(frame, text=disk_info)
        label.pack(side='left', padx=5, pady=5)

        radio = ttk.Radiobutton(frame, variable=self.selected_disk, value=disk['device'])
        radio.pack(side='right', padx=5, pady=5)

    def on_disk_selected(self, *args):
        self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        selected_disk = self.selected_disk.get()
        print(f"Selected Disk: {selected_disk}")
        from steps.filesystem_selection import FilesystemSelection
        self.parent.show_step(FilesystemSelection)
