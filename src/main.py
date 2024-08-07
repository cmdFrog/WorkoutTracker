from window import Window
from data_manager import DataManager, SettingsManager

def main():
    exercise_data = DataManager()
    user_settings = SettingsManager()
    main_window = Window(data_manager=exercise_data, user_settings=user_settings)
    main_window.run()

main()
