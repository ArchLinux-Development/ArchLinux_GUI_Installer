import tkinter as tk
from tkinter import ttk

class SearchFeature(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Search for Packages:")
        label.pack(fill='x', expand=True)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(fill='x', expand=True)

        button = ttk.Button(self, text="Search", command=self.search_packages)
        button.pack(fill='x', expand=True)

        self.search_results = tk.Text(self, height=10)
        self.search_results.pack(fill='both', expand=True)

        next_button = ttk.Button(self, text="Next", command=self.next_step)
        next_button.pack(fill='x', expand=True)

    def search_packages(self):
        query = self.search_entry.get()
        # Simulate package search
        results = f"Search results for '{query}':\nPackage1\nPackage2\nPackage3"
        self.search_results.delete(1.0, tk.END)
        self.search_results.insert(tk.END, results)

    def next_step(self):
        from steps.installation_process import InstallationProcess
        self.parent.show_step(InstallationProcess)
