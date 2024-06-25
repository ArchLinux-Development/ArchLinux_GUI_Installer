import tkinter as tk
from tkinter import ttk

class InstallationProcess(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Review and Confirm Installation:")
        label.pack(fill='x', expand=True)

        self.review_text = tk.Text(self, height=10)
        self.review_text.pack(fill='both', expand=True)

        # Simulate review details
        review_details = (
            "Selected Desktop Environment: GNOME\n"
            "Selected Software: Minimal\n"
            "Selected Filesystem: EXT4\n"
            "Username: user, Admin: True\n"
            "Hardware: Intel Core i7, NVIDIA GTX 1080, 16GB RAM\n"
            "Selected Bootloader: GRUB\n"
            "Swap File Size: 2048 MB, Zram: False\n"
            "Selected Repositories: CachyOS, Chaotic AUR\n"
            "Selected Software: Emby, Plex\n"
        )
        self.review_text.insert(tk.END, review_details)

        button = ttk.Button(self, text="Install", command=self.install)
        button.pack(fill='x', expand=True)

    def install(self):
        # Simulate the installation process
        print("Installation started...")
        # Add actual installation logic here

        completion_label = ttk.Label(self, text="Installation Complete! Reboot or chroot into the new system.")
        completion_label.pack(fill='x', expand=True)

        reboot_button = ttk.Button(self, text="Reboot", command=self.reboot)
        reboot_button.pack(fill='x', expand=True)

        chroot_button = ttk.Button(self, text="Chroot", command=self.chroot)
        chroot_button.pack(fill='x', expand=True)

    def reboot(self):
        print("Rebooting...")

    def chroot(self):
        print("Chrooting...")

