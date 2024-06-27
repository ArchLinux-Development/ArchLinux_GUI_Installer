import tkinter as tk
from tkinter import ttk
import time

class Disclaimer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
        self.start_time = time.time()  # Start the timer

    def create_widgets(self):
        label = ttk.Label(self, text="Disclaimer")
        label.pack(fill='x', padx=10, pady=5)

        self.text_box = tk.Text(self, wrap='word', height=15)
        self.text_box.pack(fill='both', expand=True, padx=10, pady=5)

        disclaimer_text = """
DISCLAIMER:

This software is provided "as is", without warranty of any kind, express or implied, 
including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
In no event shall the authors or copyright holders be liable for any claim, damages or other liability,
whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software 
or the use or other dealings in the software.

By using this software, you agree to these terms and conditions. If you do not agree, please do not use this software.
"""

        self.text_box.insert(tk.END, disclaimer_text)
        self.text_box.config(state=tk.DISABLED)

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.text_box.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.text_box.config(yscrollcommand=self.scrollbar.set)

        self.text_box.bind("<KeyRelease>", self.check_scroll)
        self.text_box.bind("<MouseWheel>", self.check_scroll)
        self.text_box.bind("<ButtonRelease-1>", self.check_scroll)

        self.agree_var = tk.BooleanVar()
        self.agree_check = ttk.Checkbutton(self, text="I have read and agree to the disclaimer", variable=self.agree_var, state=tk.DISABLED)
        self.agree_check.pack(fill='x', padx=10, pady=5)

        self.next_button = ttk.Button(self, text="Next", command=self.next_step)
        self.next_button.pack(fill='x', padx=10, pady=5)
        self.next_button.pack_forget()  # Hide the next button initially

        self.parent.after(1000, self.enable_checkbox)  # Check every second to enable the checkbox

    def enable_checkbox(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= 5 and self.text_box.yview()[1] == 1.0:  # Wait for 5 seconds and scrolling to bottom
            self.agree_check.config(state=tk.NORMAL)
        else:
            self.parent.after(1000, self.enable_checkbox)

    def check_scroll(self, event):
        if self.text_box.yview()[1] == 1.0 and self.agree_var.get():  # User has scrolled to the bottom and agreed
            self.next_button.pack(fill='x', padx=10, pady=5)  # Show the next button
            self.agree_check.config(state=tk.NORMAL)

    def next_step(self):
        if self.agree_var.get():
            from steps.desktop_selection import DesktopSelection
            self.parent.show_step(DesktopSelection)
