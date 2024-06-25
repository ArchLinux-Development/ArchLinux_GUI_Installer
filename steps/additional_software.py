import tkinter as tk
from tkinter import ttk

class AdditionalSoftware(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Additional Software and Repositories:")
        label.pack(fill='x', expand=True)

        self.repos = ["CachyOS", "Chaotic AUR"]
        self.repo_var = tk.StringVar(value=self.repos)
        self.repo_listbox = tk.Listbox(self, listvariable=self.repo_var, selectmode='multiple')
        self.repo_listbox.pack(fill='both', expand=True)

        ttk.Label(self, text="Additional Software:").pack(fill='x', expand=True)
        self.software_options = ["Emby", "Plex", "Visual Studio Code", "Browsers"]
        self.software_var = tk.StringVar(value=self.software_options)
        self.software_listbox = tk.Listbox(self, listvariable=self.software_var, selectmode='multiple')
        self.software_listbox.pack(fill='both', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        selected_repos = [self.repos[i] for i in self.repo_listbox.curselection()]
        selected_software = [self.software_options[i] for i in self.software_listbox.curselection()]
        print(f"Selected Repositories: {selected_repos}, Selected Software: {selected_software}")
        from steps.search_feature import SearchFeature
        self.parent.show_step(SearchFeature)
