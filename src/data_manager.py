import json

# pylint: disable=unspecified-encoding
class DataManager:
    def __init__(self, filename='exercise_data.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_exercise(self, date, exercise_name, reps, weight):
        if date not in self.data:
            self.data[date] = {}
        self.data[date][exercise_name] = {"reps": reps, "weight": weight}
        self.save_data()

    def get_data_for_date(self, date):
        return self.data.get(date, {})
