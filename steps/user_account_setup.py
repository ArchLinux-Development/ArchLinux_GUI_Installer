import tkinter as tk
from tkinter import ttk
import re

class UserAccountSetup(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="User Account Setup:")
        label.pack(fill='x', expand=True)

        # Username entry
        ttk.Label(self, text="Username:").pack(fill='x', expand=True)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(fill='x', expand=True)

        # Password entry
        ttk.Label(self, text="Password:").pack(fill='x', expand=True)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(fill='x', expand=True)
        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

        # Password strength meter
        self.password_strength_var = tk.StringVar()
        self.password_strength_label = ttk.Label(self, textvariable=self.password_strength_var)
        self.password_strength_label.pack(fill='x', expand=True)

        # Password confirmation entry
        ttk.Label(self, text="Confirm Password:").pack(fill='x', expand=True)
        self.password_confirm_entry = ttk.Entry(self, show="*")
        self.password_confirm_entry.pack(fill='x', expand=True)

        # Admin setup checkbox
        self.admin_var = tk.BooleanVar()
        self.admin_check = ttk.Checkbutton(self, text="Make this user an administrator", variable=self.admin_var, command=self.toggle_admin_password_entry)
        self.admin_check.pack(fill='x', expand=True)

        # Admin password entry
        self.admin_password_label = ttk.Label(self, text="Root Password:")
        self.admin_password_entry = ttk.Entry(self, show="*")

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', expand=True)

    def toggle_admin_password_entry(self):
        if self.admin_var.get():
            self.admin_password_label.pack(fill='x', expand=True)
            self.admin_password_entry.pack(fill='x', expand=True)
        else:
            self.admin_password_label.pack_forget()
            self.admin_password_entry.pack_forget()

    def check_password_strength(self, event):
        password = self.password_entry.get()
        strength = self.calculate_password_strength(password)
        self.password_strength_var.set(f"Password strength: {strength}")

    def calculate_password_strength(self, password):
        if len(password) < 6:
            return "Weak"
        strength = 0
        if len(password) >= 8:
            strength += 1
        if re.search(r"\d", password):
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 1
        if strength <= 2:
            return "Weak"
        elif strength == 3:
            return "Moderate"
        else:
            return "Strong"

    def next_step(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        is_admin = self.admin_var.get()
        admin_password = self.admin_password_entry.get() if is_admin else None

        if password != password_confirm:
            tk.messagebox.showerror("Error", "Passwords do not match!")
            return

        print(f"Username: {username}, Password: {password}, Admin: {is_admin}, Admin Password: {admin_password}")
        from steps.bootloader_selection import BootloaderSelection
        self.parent.show_step(BootloaderSelection)
