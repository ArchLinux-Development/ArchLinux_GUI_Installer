import tkinter as tk
from tkinter import ttk

class DesktopSelection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.software_options = {
            "KDE Plasma": ["Konsole", "Dolphin", "Kate", "Gwenview", "Okular", "Spectacle"],
            "GNOME": ["GNOME Terminal", "Nautilus", "Gedit", "Evince", "GNOME Screenshot"],
            "XFCE": ["XFCE Terminal", "Thunar", "Mousepad", "Ristretto", "XFCE Screenshooter"],
            "Cinnamon": ["GNOME Terminal", "Nemo", "Gedit", "Evince", "GNOME Screenshot"],
            "MATE": ["MATE Terminal", "Caja", "Pluma", "Atril", "Mate Screenshot"],
            "LXQt": ["QTerminal", "PCManFM-Qt", "FeatherPad", "LXImage-Qt", "LXQt Archiver"],
            "Budgie": ["Tilix", "Nautilus", "Gedit", "Evince", "GNOME Screenshot"],
            "i3": ["i3", "i3status", "i3lock", "dmenu"],
            "Deepin": ["Deepin Terminal", "Deepin File Manager", "Deepin Text Editor", "Deepin Image Viewer"],
            "Awesome": ["Awesome", "Rxvt-Unicode", "Dmenu", "Thunar"],
            "Bspwm": ["Bspwm", "Sxhkd", "Rxvt-Unicode", "Dmenu", "Thunar"],
            "Cutefish": ["Cutefish-Core", "Cutefish-Qt-Plugins", "Cutefish-Settings"],
            "Enlightenment": ["Enlightenment", "Terminology", "Econnman"],
            "Hyprland": ["Hyprland", "Waybar", "Alacritty", "Thunar", "Wofi"],
            "Qtile": ["Qtile", "Alacritty", "Dmenu", "Thunar"],
            "Sway": ["Sway", "Alacritty", "Thunar", "Wofi"]
        }
        self.create_widgets()

    def create_widgets(self):
        # Display detected hardware information
        hardware_label = ttk.Label(self, text="Detected Hardware Information:")
        hardware_label.pack(fill='x', expand=True)

        hardware_info = tk.Text(self, height=10, wrap='word')
        hardware_info.pack(fill='both', expand=True)

        hardware_details = (
            f"CPU: {self.parent.hardware_info['cpu_info']}\n"
            f"GPU: {self.parent.hardware_info['gpu_info']}\n"
            f"Memory: {self.parent.hardware_info['memory']} GB\n"
            f"Locale: {self.parent.hardware_info['locale']}\n"
            f"Keyboard Layout: {self.parent.hardware_info['keyboard_layout']}\n"
            f"System Type: {self.parent.hardware_info['virtualization']}\n"
        )
        hardware_info.insert(tk.END, hardware_details)
        hardware_info.config(state=tk.DISABLED)

        # Desktop environment selection
        label = ttk.Label(self, text="Select Desktop Environment:")
        label.pack(fill='x', expand=True)

        self.desktop_env = ttk.Combobox(self, values=list(self.software_options.keys()))
        self.desktop_env.pack(fill='x', expand=True)
        self.desktop_env.current(0)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_desktop = self.desktop_env.get()
        print(f"Selected Desktop Environment: {selected_desktop}")
        self.parent.selected_desktop = selected_desktop
        from steps.software_selection import SoftwareSelection
        self.parent.show_step(SoftwareSelection)
