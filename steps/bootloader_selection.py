import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class BootloaderSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.bootloaders = [
            {"name": "GRUB", "icon": "grub.png", "description": "GRUB is a boot loader package from the GNU Project. GRUB is the reference implementation of the Free Software Foundation's Multiboot Specification, which provides a user the choice to boot one of multiple operating systems installed on a computer or select a specific kernel configuration available on a particular operating system's partitions."},
            {"name": "systemd-boot", "icon": "systemd-boot.png", "description": "systemd-boot (formerly gummiboot) is a simple UEFI boot manager which executes configured EFI images. The default entry is selected by a configured pattern (glob) or an on-screen menu."},
            {"name": "rEFInd", "icon": "refind.png", "description": "rEFInd is a boot manager for UEFI and EFI-based machines. It was derived from and extends the capabilities of the rEFIt boot manager, adding a more GUI-like interface and better support for Linux."},
            {"name": "LILO", "icon": "lilo.png", "description": "LILO (LInux LOader) is a boot loader for Linux and was the default boot loader for most Linux distributions in the years prior to the popularity of GRUB."}
        ]
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Bootloader:")
        label.pack(fill='x', expand=True)

        self.bl_frame = ttk.Frame(self)
        self.bl_frame.pack(fill='both', expand=True)

        self.bl_icons = {}
        self.selected_bl = tk.StringVar()
        self.selected_bl.trace('w', self.on_bl_selected)

        for bl in self.bootloaders:
            self.add_bootloader_option(bl["name"], bl["icon"], bl["description"])

        self.next_button = ttk.Button(self, text="Next", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(fill='x', expand=True, pady=10)

    def add_bootloader_option(self, name, icon_path, description):
        frame = ttk.Frame(self.bl_frame)
        frame.pack(fill='x', expand=True, padx=5, pady=5)

        icon = self.load_icon(icon_path)
        icon_label = ttk.Label(frame, image=icon)
        icon_label.image = icon  # Keep a reference to avoid garbage collection
        icon_label.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        label = ttk.Label(frame, text=name)
        label.grid(row=0, column=1, sticky='w')

        description_label = ttk.Label(frame, text=description, wraplength=400, justify='left')
        description_label.grid(row=1, column=1, sticky='w')

        radio = ttk.Radiobutton(frame, variable=self.selected_bl, value=name)
        radio.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

    def load_icon(self, icon_path):
        icon_full_path = os.path.join("icons", icon_path)
        image = Image.open(icon_full_path)
        image = image.resize((32, 32), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def on_bl_selected(self, *args):
        self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        selected_bl = self.selected_bl.get()
        if not selected_bl:
            print("No bootloader selected")
            return
        print(f"Selected Bootloader: {selected_bl}")
        self.parent.selected_bootloader = selected_bl
        from steps.desktop_selection import DesktopSelection
        self.parent.show_step(DesktopSelection)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bootloader Selection")
    BootloaderSelection(root).pack(fill='both', expand=True)
    root.mainloop()
