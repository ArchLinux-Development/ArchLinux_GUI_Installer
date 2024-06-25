import tkinter as tk
from tkinter import ttk

class SoftwareSelection(ttk.Frame):
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
            "Deepin": ["Deepin Terminal", "Deepin File Manager", "Deepin Text Editor", "Deepin Image Viewer"]
        }
        self.create_widgets()

    def create_widgets(self):
        selected_desktop = self.parent.selected_desktop
        label = ttk.Label(self, text=f"Select Software Options for {selected_desktop}:")
        label.pack(fill='x', expand=True)

        self.software_list = self.software_options.get(selected_desktop, [])
        self.software_var = tk.StringVar(value=self.software_list)
        self.software_listbox = tk.Listbox(self, listvariable=self.software_var, selectmode='multiple')
        self.software_listbox.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_software_indices = self.software_listbox.curselection()
        selected_software = [self.software_list[i] for i in selected_software_indices]
        print(f"Selected Software: {selected_software}")
        self.parent.selected_software = selected_software
        from steps.filesystem_selection import FilesystemSelection
        self.parent.show_step(FilesystemSelection)
