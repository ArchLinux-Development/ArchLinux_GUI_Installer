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

        container = ttk.Frame(self)
        container.pack(fill='both', expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(container, columns=("Device", "Total", "Used", "Free", "Partitions"), show="headings")
        self.tree.heading("Device", text="Device")
        self.tree.heading("Total", text="Total (GB)")
        self.tree.heading("Used", text="Used (GB)")
        self.tree.heading("Free", text="Free (GB)")
        self.tree.heading("Partitions", text="Partitions")

        self.tree.column("Device", anchor='w', width=100)
        self.tree.column("Total", anchor='center', width=100)
        self.tree.column("Used", anchor='center', width=100)
        self.tree.column("Free", anchor='center', width=100)
        self.tree.column("Partitions", anchor='w', width=300)

        self.scrollbar = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")
        self.tree.pack(fill='both', expand=True)

        for disk in self.disks:
            partitions_info = ', '.join([f"{p['mountpoint']} ({p['fstype']})" for p in self.disks[disk]["partitions"]])
            self.tree.insert("", "end", values=(
                disk,
                f"{self.disks[disk]['total']:.2f}",
                f"{self.disks[disk]['used']:.2f}",
                f"{self.disks[disk]['free']:.2f}",
                partitions_info
            ))

        self.tree.bind("<ButtonRelease-1>", self.on_item_selected)

        self.selected_disk = None
        self.next_button = ttk.Button(self, text="Next", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(fill='x', expand=True, padx=10, pady=10)

    def get_disks(self):
        disks = {}
        partitions = psutil.disk_partitions(all=False)
        for partition in partitions:
            device = partition.device.split('p')[0]  # Handles /dev/sda1, /dev/sda2, etc.
            if device not in disks:
                disks[device] = {
                    "partitions": [],
                    "total": psutil.disk_usage(partition.mountpoint).total / (1024 ** 3),
                    "used": psutil.disk_usage(partition.mountpoint).used / (1024 ** 3),
                    "free": psutil.disk_usage(partition.mountpoint).free / (1024 ** 3)
                }
            disks[device]["partitions"].append({
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype
            })
        return disks

    def on_item_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.selected_disk = self.tree.item(selected_item)["values"][0]
            self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        if self.selected_disk:
            if self.disks[self.selected_disk]['used'] > 0:
                result = messagebox.askyesno("Warning", f"The selected disk {self.selected_disk} is not empty. Do you want to proceed?")
                if not result:
                    return
            print(f"Selected Disk: {self.selected_disk}")
            from steps.filesystem_selection import FilesystemSelection
            self.parent.show_step(FilesystemSelection)
