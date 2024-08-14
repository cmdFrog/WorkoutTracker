from datetime import datetime
import json

# pylint: disable=unspecified-encoding
class DataManager:
    def __init__(self, filename="exercise_data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"exercises": [], "data": {}}  # Separate exercise list and data dictionary

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file)
        # Reload the in memory data
        self.data = self.load_data()

    def add_exercise_name(self, exercise_name):
        # Check if the lowercase exercise name is not in the list (also in lowercase)
        if exercise_name.lower() not in [exercise.lower() for exercise in self.data["exercises"]]:
            # Add the exercise name as is
            self.data["exercises"].append(exercise_name)
            # Save the updated data
            self.save_data()

    def remove_exercise_name(self, exercise_name):
        self.data["exercises"].remove(exercise_name)
        # Save the updated data
        self.save_data()

    def get_exercises(self):
        return self.data.get("exercises", [])

    def add_exercise_entry(self, date, exercise_name, reps, weight):
        if date not in self.data["data"]:
            self.data["data"][date] = {}
        self.data["data"][date][exercise_name] = {"reps": reps, "weight": weight}
        self.save_data()

    def remove_exercise_entry(self, date, exercise_name):
        if date in self.data["data"]:
            del self.data["data"][date][exercise_name]

    def get_data(self, date):
        return self.data.get("data", {}).get(date, {})

    def get_data_in_range(self, from_date, to_date):
        data_in_range = []

        from_date = datetime.strptime(from_date, "%m/%d/%Y")
        to_date = datetime.strptime(to_date, "%m/%d/%Y")

        for date_str, exercises in self.data.get("data", {}).items():
            # Convert the date string in the data to a datetime object
            date = datetime.strptime(date_str, "%m/%d/%Y")
            if from_date <= date <= to_date:
                for exercise_name, exercise_data in exercises.items():
                    # Append relevant data
                    data_in_range.append({
                        "date": date_str,
                        "exercise": exercise_name,
                        **exercise_data
                    })

        return data_in_range

# Currently unused until Settings features implemented
class SettingsManager:
    def __init__(self, filename="user_settings.json"):
        self.default_settings = "default_settings.json"
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.default_settings, "r") as file:
                return json.load(file)  # Return default settings if user_settings doesn't exist

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def get_data(self, setting):
        return self.data.get(setting, {})
