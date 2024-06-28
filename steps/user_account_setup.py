import tkinter as tk
from tkinter import ttk, messagebox
import re
import psutil
import subprocess

class UserAccountSetup(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.hardware_info = self.detect_hardware()
        self.create_widgets()

    def detect_hardware(self):
        info = {}
        info['cpu'] = psutil.cpu_count(logical=True)
        info['memory'] = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert bytes to GB

        try:
            result = subprocess.run(['lscpu'], capture_output=True, text=True)
            info['cpu_info'] = self.extract_cpu_model(result.stdout)
        except Exception as e:
            info['cpu_info'] = str(e)

        try:
            result = subprocess.run(['lspci', '-mm'], capture_output=True, text=True)
            info['gpu_info'] = self.extract_gpu_models(result.stdout)
        except Exception as e:
            info['gpu_info'] = str(e)

        try:
            result = subprocess.run(['locale'], capture_output=True, text=True)
            info['locale'] = result.stdout.strip()
        except Exception as e:
            info['locale'] = str(e)

        try:
            result = subprocess.run(['localectl', 'status'], capture_output=True, text=True)
            info['keyboard_layout'] = self.extract_keyboard_layout(result.stdout)
        except Exception as e:
            info['keyboard_layout'] = str(e)

        try:
            result = subprocess.run(['dmidecode', '-s', 'system-product-name'], capture_output=True, text=True)
            info['virtualization'] = self.detect_virtualization(result.stdout)
        except Exception as e:
            info['virtualization'] = str(e)

        return info

    def extract_cpu_model(self, lscpu_output):
        for line in lscpu_output.split('\n'):
            if 'Model name' in line:
                return line.split(':')[1].strip()
        return "Unknown CPU"

    def extract_gpu_models(self, lspci_output):
        gpus = []
        for line in lspci_output.split('\n'):
            if 'VGA compatible controller' in line or '3D controller' in line:
                parts = line.split('"')
                if len(parts) > 3:
                    gpus.append(parts[3])
                else:
                    gpus.append(parts[1])
        return ', '.join(gpus) if gpus else "Unknown GPU"

    def extract_keyboard_layout(self, localectl_output):
        for line in localectl_output.split('\n'):
            if 'Layout' in line:
                return line.split(': ')[1].strip()
        return "Unknown Layout"

    def detect_virtualization(self, dmidecode_output):
        if 'VirtualBox' in dmidecode_output:
            return 'VirtualBox'
        else:
            return 'Physical Machine'

    def create_widgets(self):
        self.pack(fill='both', expand=True, padx=10, pady=10)

        label = ttk.Label(self, text="Hardware Information")
        label.pack(fill='x', padx=10, pady=5)

        # Display hardware information
        hw_info_frame = ttk.Frame(self)
        hw_info_frame.pack(fill='x', padx=10, pady=5)
        for key, value in self.hardware_info.items():
            ttk.Label(hw_info_frame, text=f"{key}: {value}").pack(fill='x', padx=10, pady=2)
        ttk.Label(hw_info_frame, text=f"GPU(s): {self.hardware_info['gpu_info']}").pack(fill='x', padx=10, pady=2)

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x', pady=10)

        label = ttk.Label(self, text="User Account Setup")
        label.pack(fill='x', padx=10, pady=5)

        user_frame = ttk.Frame(self)
        user_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.admin_var = tk.BooleanVar()
        self.admin_check = ttk.Checkbutton(user_frame, text="Make user a SuperUser", variable=self.admin_var)
        self.admin_check.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        ttk.Label(user_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.username_entry = ttk.Entry(user_frame)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(user_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.password_entry = ttk.Entry(user_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

        ttk.Label(user_frame, text="Confirm Password:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.password_confirm_entry = ttk.Entry(user_frame, show="*")
        self.password_confirm_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.password_strength_var = tk.StringVar()
        self.password_strength_label = ttk.Label(user_frame, textvariable=self.password_strength_var)
        self.password_strength_label.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(user_frame, text="Root Password:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.admin_password_entry = ttk.Entry(user_frame, show="*")
        self.admin_password_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(user_frame, text="Confirm Root Password:").grid(row=6, column=0, padx=5, pady=5, sticky='e')
        self.admin_password_confirm_entry = ttk.Entry(user_frame, show="*")
        self.admin_password_confirm_entry.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        button = ttk.Button(self, text="Next", command=self.next_step)
        button.pack(fill='x', padx=10, pady=20)

    def check_password_strength(self, event):
        password = self.password_entry.get()
        strength = self.calculate_password_strength(password)
        self.password_strength_var.set(f"Password strength: {strength}")

    def calculate_password_strength(self, password):
        if len(password) < 8:
            return "Too short"
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
        admin_password = self.admin_password_entry.get()
        admin_password_confirm = self.admin_password_confirm_entry.get()

        if password != password_confirm:
            messagebox.showerror("Error", "User passwords do not match!")
            return

        if admin_password != admin_password_confirm:
            messagebox.showerror("Error", "Root passwords do not match!")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "User password must be at least 8 characters long!")
            return

        if len(admin_password) < 8:
            messagebox.showerror("Error", "Root password must be at least 8 characters long!")
            return

        print(f"Username: {username}, Password: {password}, SuperUser: {is_admin}, Admin Password: {admin_password}")
        from steps.disk_selection import DiskSelection
        self.parent.show_step(DiskSelection)
