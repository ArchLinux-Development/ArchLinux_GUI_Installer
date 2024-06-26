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
