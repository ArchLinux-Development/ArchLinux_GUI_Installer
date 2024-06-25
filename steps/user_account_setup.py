import tkinter as tk
from tkinter import ttk

class UserAccountSetup(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="User Account Setup:")
        label.pack(fill='x', expand=True)

        ttk.Label(self, text="Username:").pack(fill='x', expand=True)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(fill='x', expand=True)

        ttk.Label(self, text="Password:").pack(fill='x', expand=True)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(fill='x', expand=True)

        self.admin_var = tk.BooleanVar()
        self.admin_check = ttk.Checkbutton(self, text="Make this user an administrator", variable=self.admin_var)
        self.admin_check.pack(fill='x', expand=True)

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def next_step(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        is_admin = self.admin_var.get()
        print(f"Username: {username}, Password: {password}, Admin: {is_admin}")
        from steps.hardware_detection import HardwareDetection
        self.parent.show_step(HardwareDetection)
