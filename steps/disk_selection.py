import tkinter as tk
from tkinter import ttk, messagebox
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
        disks = {}
        for disk in psutil.disk_partitions(all=False):
            device = disk.device.split('p')[0]  # Handles /dev/sda1, /dev/sda2, etc.
            if device not in disks:
                disks[device] = {
                    "partitions": [],
                    "total": psutil.disk_usage(disk.mountpoint).total / (1024 ** 3),
                    "used": psutil.disk_usage(disk.mountpoint).used / (1024 ** 3),
                    "free": psutil.disk_usage(disk.mountpoint).free / (1024 ** 3)
                }
            disks[device]["partitions"].append({
                "mountpoint": disk.mountpoint,
                "fstype": disk.fstype
            })
        return disks

    def add_disk_option(self, disk):
        frame = ttk.Frame(self.disk_frame)
        frame.pack(fill='x', expand=True, padx=5, pady=5)

        disk_info = f"{disk} - Total: {self.disks[disk]['total']:.2f} GB, Used: {self.disks[disk]['used']:.2f} GB, Free: {self.disks[disk]['free']:.2f} GB"
        label = ttk.Label(frame, text=disk_info)
        label.pack(side='left', padx=5, pady=5)

        partitions_info = ', '.join([f"{p['mountpoint']} ({p['fstype']})" for p in self.disks[disk]["partitions"]])
        partitions_label = ttk.Label(frame, text=f"Partitions: {partitions_info}")
        partitions_label.pack(side='left', padx=5, pady=5)

        radio = ttk.Radiobutton(frame, variable=self.selected_disk, value=disk)
        radio.pack(side='right', padx=5, pady=5)

    def on_disk_selected(self, *args):
        self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        selected_disk = self.selected_disk.get()
        if self.disks[selected_disk]['used'] > 0:
            result = messagebox.askyesno("Warning", f"The selected disk {selected_disk} is not empty. Do you want to proceed?")
            if not result:
                return
        print(f"Selected Disk: {selected_disk}")
        from steps.filesystem_selection import FilesystemSelection
        self.parent.show_step(FilesystemSelection)
