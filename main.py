import tkinter as tk
from tkinter import ttk

try:
    from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
    from mock_archinstall.default_profiles.xorg import XorgProfile
except ImportError:
    from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
    from mock_archinstall.default_profiles.xorg import XorgProfile

from desktops import (
    PlasmaProfile, GnomeProfile, XfceProfile,
    CinnamonProfile, MateProfile, LxqtProfile,
    BudgieProfile, I3Profile, DeepinProfile,
    AwesomeProfile, BspwmProfile, CutefishProfile,
    EnlightenmentProfile, HyprlandProfile, QtileProfile, SwayProfile
)

class ArchLinuxInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arch Linux GUI Installer")
        self.geometry("800x815")
        self.minsize(800, 700)
        self.current_step = None
        self.selected_desktop = None
        self.selected_software = None
        self.show_step(Disclaimer)

    def show_step(self, step_class):
        if self.current_step:
            self.current_step.destroy()
        self.current_step = step_class(self)
        self.current_step.pack(fill='both', expand=True)

if __name__ == "__main__":
    from steps.disclaimer import Disclaimer
    from steps.user_account_setup import UserAccountSetup
    from steps.disk_selection import DiskSelection
    from steps.filesystem_selection import FilesystemSelection
    from steps.swap_file_configuration import SwapFileConfiguration
    from steps.bootloader_selection import BootloaderSelection

    app = ArchLinuxInstaller()
    app.show_step(Disclaimer)
    app.mainloop()
