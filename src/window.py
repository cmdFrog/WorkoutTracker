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
        self.add_exercise_status = ttk.Label(add_exercise, text="", font="Helvetica 10 bold")

        # place add_exercise widgets
        add_exercise.columnconfigure(0, pad=20, weight=1)
        add_exercise.rowconfigure(0, pad=10, weight=1)
        add_exercise.rowconfigure(1, pad=10, weight=1)
        add_exercise.rowconfigure(2, pad=10, weight=1)
        self.exercise_entry.grid(row=0, column=0, sticky='ew', padx=20)
        self.exercise_button.grid(row=1, column=0)
        self.exercise_entry.bind('<Return>', self.add_exercise_to_database)
        self.exercise_entry.bind('<KP_Enter>', self.add_exercise_to_database)
        self.add_exercise_status.grid(row=2, column=0)

        # input_frame widgets
        self.date_label = ttk.Label(input_frame, text="Select Date:", font="Helvetica 10 bold")
        self.date_entry = ttk.DateEntry(input_frame)
        self.date_var = ttk.StringVar()
        self.date_var.trace_add("write", lambda name, index, mode, date_var = self.date_var: self.update_date(self.date_var)) # Date change updates label
        self.date_entry.entry.configure(textvariable=self.date_var)

        select_exercise_label = ttk.Label(input_frame, text="Select Exercise:", font="Helvetica 10 bold")
        self.exercise_dropdown = ttk.Combobox(input_frame, state="readonly", font="Helvetica 10 bold")
        self.exercise_dropdown['values'] = self.exercise_items
        self.remove_exercise_button = ttk.Button(input_frame, text="Remove Exercise From List", command=self.remove_exercise_from_database)

        weight_label = ttk.Label(input_frame, text="Enter Weight:", font="Helvetica 10 bold")
        self.weight_entry = ttk.Entry(input_frame, validate="key", validatecommand=(self.window.register(self.validate_number_only), "%P"))

        reps_label = ttk.Label(input_frame, text="Enter Reps:", font="Helvetica 10 bold")
        self.reps_entry = ttk.Entry(input_frame, validate="key", validatecommand=(self.window.register(self.validate_number_only), "%P"))

        data_submit_button = ttk.Button(input_frame, text="Submit Data", command=self.add_exercise_info_to_db)
        self.data_submit_label = ttk.Label(input_frame, font="Helvetica 10 bold")

        # place input_frame widgets
        input_frame.columnconfigure(0, pad = 10, weight=1)
        input_frame.columnconfigure(1, pad = 10, weight=1)
        input_frame.columnconfigure(2, pad = 10, weight=1)
        input_frame.rowconfigure(0, pad = 10, weight = 2)
        input_frame.rowconfigure(1, pad = 10, weight = 2)
        input_frame.rowconfigure(2, pad = 10, weight = 2)
        input_frame.rowconfigure(3, pad = 10, weight = 2)
        input_frame.rowconfigure(4, pad = 10, weight = 2)

        self.date_label.grid(row=0, column=0)
        self.date_entry.grid(row=0, column=1)
        select_exercise_label.grid(row=1, column=0)
        self.exercise_dropdown.grid(row=1, column=1)
        self.remove_exercise_button.grid(row=1, column=2)
        weight_label.grid(row=2, column=0)
        self.weight_entry.grid(row=2, column=1)
        reps_label.grid(row=3, column=0)
        self.reps_entry.grid(row=3, column=1)
        data_submit_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20)
        self.data_submit_label.grid(row=4, column=2)

        # create treeview widgets
        tree_style = ttk.Style()
        tree_style.configure("Treeview.Heading", font="Helvetica 15 bold", relief="groove")
        tree_style.configure("Treeview.Cell", font="Helvetica 12 bold")
        tree_style.configure("Treeview", rowheight=30)
        self.workouts_table = ttk.Treeview(treeview_frame, columns=("exercise", "weight", "reps"), show="headings")
        self.workouts_table.bind("<Delete>", self.remove_exercise_info_from_db)
        self.workouts_table.heading("exercise", text="Exercise", anchor="center")
        self.workouts_table.heading("weight", text="Weight", anchor="center")
        self.workouts_table.heading("reps", text="Reps", anchor="center")
        self.workouts_table.column("exercise", anchor="center")
        self.workouts_table.column("weight", anchor="center")
        self.workouts_table.column("reps", anchor="center")

        tree_scroll = ttk.Scrollbar(treeview_frame, command=self.workouts_table.yview)
        self.workouts_table.configure(yscrollcommand=tree_scroll.set)

        # workouts_table.insert(parent = "", index=0, values=("Goofing Around", "100", "1000"))
        # for _ in range(0, 100):
        #     workouts_table.insert(parent = "", index=0, values=("Goofing Around", "100", "1000"))


        # place treeview widgets
        self.workouts_table.pack(fill='both', expand=True, side="left")
        tree_scroll.pack(side="left", fill="both")

        # create and pack Label and button for treeview date and deleting
        self.selected_date_label = ttk.Label(treeview_date_frame, text="", font="Helvetica 15 bold")
        self.selected_date_label.pack(anchor="center")
        self.entry_remove_button = ttk.Button(treeview_date_frame, text="Delete Selection", command=self.remove_exercise_info_from_db)
        self.entry_remove_button.pack(anchor="center")

    def update_date(self, var):
        selected_date = var.get()
        if selected_date == "":
            return
        date_object = datetime.strptime(selected_date, "%m/%d/%Y")
        formated_date = date_object.strftime("%A, %b %d, %Y")
        self.selected_date_label.config(text=f"Selected Date: {formated_date}")
        self.update_tree_view(date=selected_date)

    def update_tree_view(self, date):
        self.clear_treeview()
        data = self.data_manager.get_data(date)
        if data:
            for exercise, details in data.items():
                reps_value = details.get("reps", "N/A")
                weight_value = details.get("weight", "N/A")
                self.workouts_table.insert(parent="", index=0, values=(exercise, weight_value, reps_value))


    def add_exercise_to_database(self, _=None):
        exercise_name = self.exercise_entry.get()
        if exercise_name:
            self.data_manager.add_exercise_name(exercise_name)
            self.exercise_items = self.data_manager.get_exercises()
            self.exercise_dropdown['values'] = self.exercise_items
            self.add_exercise_status.configure(text=f"Exercise Added: {exercise_name}", foreground='green')
            self.exercise_entry.delete(0, 'end')

    def clear_treeview(self):
        # Get all child items in the Treeview and delete them
        for item in self.workouts_table.get_children():
            self.workouts_table.delete(item)

    def remove_exercise_from_database(self, _=None):
        exercise_name = self.exercise_dropdown.get()
        if exercise_name:
            self.data_manager.remove_exercise_name(exercise_name)
            self.exercise_items = self.data_manager.get_exercises()
            self.exercise_dropdown['values'] = self.exercise_items
            self.exercise_dropdown.set('')
            self.add_exercise_status.configure(text=f"Exercise Removed: {exercise_name}", foreground='red')

    def add_exercise_info_to_db(self):
        date = self.date_var.get()
        exercise_name = self.exercise_dropdown.get()
        weight = self.weight_entry.get()
        reps = self.reps_entry.get()
        if date == "" or exercise_name == "" or weight == "" or reps == "":
            self.data_submit_label.configure(text="Missing data", foreground="red")
        else:
            self.data_submit_label.configure(text="Submit Successful", foreground="green")
            self.data_manager.add_exercise_entry(date, exercise_name, reps, weight)
            self.update_tree_view(date)

    def remove_exercise_info_from_db(self, _=None):
        date = self.date_var.get()
        for i in self.workouts_table.selection():
            #print(self.workouts_table.item(i)['values'][0])
            exercise = self.workouts_table.item(i)['values'][0]
            self.workouts_table.delete(i)
            self.data_manager.remove_exercise_entry(date=str(date), exercise_name=str(exercise))
            self.data_manager.save_data()


    def data_graphing_widgets(self):
        pass

    def validate_number_only(self, new_value):
        if new_value.isdigit() or new_value == "":
            return True
        return False
