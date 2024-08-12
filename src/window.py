#import tkinter as tk
#from tkinter import ttk
from datetime import datetime
import ttkbootstrap as ttk

class Window:
    def __init__(self, data_manager, user_settings):
        # init window
        self.window = ttk.Window(themename="darkly")
        self.window.title("Workout Tracker")
        self.window.geometry(f"{int(self.window.winfo_screenwidth() * 0.6)}x{int(self.window.winfo_screenheight() * 0.6)}")
        #self.window.minsize(height=int(self.window.winfo_screenheight() * 0.6), width=int(self.window.winfo_screenwidth() * 0.6))
        # variables for data manager and user settings
        self.data_manager = data_manager
        self.user_settings = user_settings
        self.exercise_items = self.data_manager.get_exercises()
        # apply settings to window and style
        #self.set_settings()
        # create tabs
        self.tabs()
        # widgets for data_input tab
        self.data_input_widgets()
        # widgets for data_graphing tab
        self.data_graphing_widgets()

    def run(self):
        self.window.mainloop()
        print("Window closed")

    #def set_settings(self):
        #self.window.configure(bg=self.user_settings.get_data("bg_color"))
        #self.fr_style = ttk.Style()
        #self.fr_style.configure("TFrame", background=self.user_settings.get_data("bg_color"))

    def tabs(self):
        # Create tabs
        tabs = ttk.Notebook(self.window)
        self.data_input = ttk.Frame(tabs)
        self.data_graphing = ttk.Frame(tabs)
        self.settings_tab = ttk.Frame(tabs)

        # Add tabs
        tabs.add(self.data_input, text="Data Input")
        tabs.add(self.data_graphing, text="Data Graphing")
        tabs.add(self.settings_tab, text="Settings")

        # Pack tabs
        tabs.pack(expand=True, fill='both')

    def data_input_widgets(self):
        # Create Frames
        add_exercise = ttk.LabelFrame(self.data_input, text="Add New Exercise To Dropdown", bootstyle="info")
        input_frame = ttk.LabelFrame(self.data_input, text="Add Each Exercise For Selected Date", bootstyle="info")
        treeview_frame = ttk.LabelFrame(self.data_input, text="Exercises Submitted For Selected Date", bootstyle="info")
        treeview_date_frame = ttk.LabelFrame(self.data_input, text="Selected Date", bootstyle="info")

        # Place frames
        add_exercise.place(relx=0, rely=0, relheight=0.2, relwidth=0.4)
        input_frame.place(relx=0, rely=0.2, relheight=0.8, relwidth=0.4)
        treeview_frame.place(relx=0.41, rely=0, relheight=0.9, relwidth=0.59)
        treeview_date_frame.place(relx=0.41, rely=0.9, relheight=0.1, relwidth=0.59)

        # add_exercise frame widgets
        self.exercise_entry = ttk.Entry(add_exercise)
        self.exercise_button = ttk.Button(add_exercise, text="Submit Exercise", command=self.add_exercise_to_database)

        # place add_exercise widgets
        add_exercise.columnconfigure(0, pad=20, weight=1)
        add_exercise.rowconfigure(0, pad=10, weight=1)
        add_exercise.rowconfigure(1, pad=10, weight=1)
        self.exercise_entry.grid(row=0, column=0, sticky='ew', padx=20)
        self.exercise_button.grid(row=1, column=0)

        # input_frame widgets
        self.date_label = ttk.Label(input_frame, text="Select Date:", font="Helvetica 10 bold")
        self.date_entry = ttk.DateEntry(input_frame)
        # self.date_entry.bind("<<DateEntrySelected>>", self.update_date_label)
        date_var = ttk.StringVar()
        date_var.trace_add("write", lambda name, index, mode, date_var = date_var: self.update_date_label(date_var))
        self.date_entry.entry.configure(textvariable=date_var)

        select_exercise_label = ttk.Label(input_frame, text="Select Exercise:", font="Helvetica 10 bold")
        exercise_dropdown = ttk.Combobox(input_frame, state="readonly", font="Helvetica 10 bold")
        exercise_dropdown['values'] = self.exercise_items

        weight_label = ttk.Label(input_frame, text="Enter Weight:", font="Helvetica 10 bold")
        weight_entry = ttk.Entry(input_frame)

        reps_label = ttk.Label(input_frame, text="Enter Reps:", font="Helvetica 10 bold")
        reps_entry = ttk.Entry(input_frame)

        data_submit_button = ttk.Button(input_frame, text="Submit")

        # place input_frame widgets
        input_frame.columnconfigure(0, pad = 10, weight=1)
        input_frame.columnconfigure(1, pad = 10, weight=1)
        input_frame.rowconfigure(0, pad = 10, weight = 2)
        input_frame.rowconfigure(1, pad = 10, weight = 2)
        input_frame.rowconfigure(2, pad = 10, weight = 2)
        input_frame.rowconfigure(3, pad = 10, weight = 2)
        input_frame.rowconfigure(4, pad = 10, weight = 2)

        self.date_label.grid(row=0, column=0)
        self.date_entry.grid(row=0, column=1)
        select_exercise_label.grid(row=1, column=0)
        exercise_dropdown.grid(row=1, column=1)
        weight_label.grid(row=2, column=0)
        weight_entry.grid(row=2, column=1)
        reps_label.grid(row=3, column=0)
        reps_entry.grid(row=3, column=1)
        data_submit_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20)

        # create treeview widgets
        tree_style = ttk.Style()
        tree_style.configure("Treeview.Heading", font="Helvetica 15 bold", relief="groove")
        tree_style.configure("Treeview.Cell", font="Helvetica 12 bold")
        tree_style.configure("Treeview", rowheight=30)
        workouts_table = ttk.Treeview(treeview_frame, columns=("exercise", "weight", "reps"), show="headings")
        workouts_table.heading("exercise", text="Exercise", anchor="center")
        workouts_table.heading("weight", text="Weight", anchor="center")
        workouts_table.heading("reps", text="Reps", anchor="center")
        workouts_table.column("exercise", anchor="center")
        workouts_table.column("weight", anchor="center")
        workouts_table.column("reps", anchor="center")

        tree_scroll = ttk.Scrollbar(treeview_frame, command=workouts_table.yview)
        workouts_table.configure(yscrollcommand=tree_scroll.set)

        # workouts_table.insert(parent = "", index=0, values=("Goofing Around", "100", "1000"))
        # for _ in range(0, 100):
        #     workouts_table.insert(parent = "", index=0, values=("Goofing Around", "100", "1000"))


        # place treeview widgets
        workouts_table.pack(fill='both', expand=True, side="left")
        tree_scroll.pack(side="left", fill="both")

        # create and pack Label for treeview date
        self.selected_date_label = ttk.Label(treeview_date_frame, text="", font="Helvetica 15 bold")
        self.selected_date_label.pack(anchor="center")

    def update_date_label(self, var):
        selected_date = var.get()
        if selected_date == "":
            return
        date_object = datetime.strptime(selected_date, "%m/%d/%Y")
        formated_date = date_object.strftime("%A, %b %d")
        self.selected_date_label.config(text=f"Selected Date: {formated_date}")

    def add_exercise_to_database(self):
        exercise_name = self.exercise_entry.get()
        if exercise_name:
            self.data_manager.add_exercise_name(exercise_name)
            self.exercise_items = self.data_manager.get_exercises()
        return


    def data_graphing_widgets(self):
        pass

    def validate_number_only(self, new_value):
        if new_value.isdigit() or new_value == "":
            return True
        return False
