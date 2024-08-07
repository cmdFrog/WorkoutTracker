import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Test")
        self.window.geometry("800x500")
        self.widgets()

    def run(self):
        self.window.mainloop()
        print("Window closed")

    def widgets(self):
        pass
