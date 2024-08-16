# WorkoutTracker

WorkoutTracker is a Python GUI application using TKinter (specifically ttkbootstrap) for recording the reps and weight for an exercise on a given date. Your data can then be graphed to visualize progress. More features are planned for the future.

## Installation

1. Install or update Python.
2. Clone the repo to your location of choice or download as a zip file and extract.
2. Navigate to your install location in your operating system's terminal and make sure you have all the requirements.
    * ```
      pip install -r requirements.txt
3. Launch from main.py in the /src directory or from the .bat/.sh files in the main directory.
4. To create a desktop shortcut, create a shortcut to the correct .bat(Windows) or .sh(Linux/Mac) and place it on your desktop.

## Usage

WorkoutTracker currently has two tabs. Data Input and Data Graphing. The settings tab is a placeholder for future planned features. Below are detailed instructions and descriptions of functionality, but it should be mostly intuitive to just get started with.

### Data Input Tab

#### Add New Exercise To Dropdown:

In this section you can populate the dropdown menu in the next section with exercises you want to create data for.

#### Add Each Exercise For Selected Date:

This section is where you provide all the required data for each day.
* When you select a date, the table on the right side of the window will populate with all the current data for that date.
* Select an exercise from the list you added exercise names to. Here selected exercise names can be deleted. Currently, this does not remove data for that exercise, but the data can be deleted manually in the next section.
* Enter the weight you used for that day.
* Enter how many reps you had for this exercise and weight.
* Use the submit button to add this datapoint.

#### Exercises Submitted For Selected Date:

This is the table on the right side of the window. It will automatically populate with all data for the chosen date in the previous section. Data can be deleted by selecting the data you want removed, and either clicking the 'Delete Selection' button or pressing the Delete key on your keyboard.

### Data Graphing Tab

#### Graph Settings:
Here you will find all your options for what is displayed in the graph above this section.
* Select a 'from' and 'to' date to create a range of data you want graphed.
* A dropdown menu will populate with all exercises done in the chosen date range. Select and exercise to graph.
* There are two checkboxes that allow you to choose if weight, reps or both will be plotted.

## Roadmap

These are the currently planned features in development.

#### Data Input Tab:

* More sophisticated options for data preview table:
    - Mass deletion of all the data for a certain exercise.
    - Mass renaming of the exercise title for all the data for a certain exercise.
    - Option to open a new window or tab that contains an extended table view, allowing and overview of all availible data at once. Mass deletion and renaming may be in this window.

#### Data Graphing Tab:

* More graphing options:
    - Allow all data to be graphed without choosing a date range.
    - Display the date range tha encompasses all data so the user can more easily select date ranges they have data for.

#### Settings Tab:
* Change Theme:
    - Will mostly likely only have a few of the tkbootstrap themes to choose from, as certain widgets like the graph will need to be changed to match each theme.

* Data Profiles:
    - Multiple profiles for recording data
    - Not certain if this will be in settings to swtich all functionality between data sets, or will be extra options in Data Input and Graphing. The latter may allow graphing two or more profiles on the same graph to compare two people.