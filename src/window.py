import tkinter as tk
from tkinter import ttk
#import customtkinter as ctk
#import ttkbootstrap as ttk

class Window:
    def __init__(self, data_manager, user_settings):
        # init window
        self.window = tk.Tk()
        self.window.title("Workout Tracker")
        self.window.geometry(f"{int(self.window.winfo_screenwidth() * 0.6)}x{int(self.window.winfo_screenheight() * 0.6)}")
        # variables for data manager and user settings
        self.data_manager = data_manager
        self.user_settings = user_settings
        # apply settings to window and style
        self.set_settings()
        # create tabs
        self.tabs()
        # widgets for data_input tab
        self.data_input_widgets()
        # widgets for data_graphing tab
        self.data_graphing_widgets()

    def run(self):
        self.window.mainloop()
        print("Window closed")

    def set_settings(self):
        self.window.configure(bg=self.user_settings.get_data("bg_color"))
        self.fr_style = ttk.Style()
        self.fr_style.configure("TFrame", background=self.user_settings.get_data("bg_color"))

    def tabs(self):
        # Create tabs
        tabs = ttk.Notebook(self.window)
        data_input = ttk.Frame(tabs)
        data_graphing = ttk.Frame(tabs)
        settings_tab = ttk.Frame(tabs)

        # Add tabs
        tabs.add(data_input, text="Data Input")
        tabs.add(data_graphing, text="Data Graphing")
        tabs.add(settings_tab, text="Settings")

        # Pack tabs
        tabs.pack(expand=True, fill='both')

    def data_input_widgets(self):
        pass

    def data_graphing_widgets(self):
        pass