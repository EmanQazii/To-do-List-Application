# To-Do List Application

## Overview

This is a Python-based console application designed to help users manage their tasks efficiently. The application allows users to add, view, delete, update, and search for tasks. Each task is stored with a description, priority, and due date in a CSV file (`task.csv`).

## Features

- **Add Tasks**: Add multiple tasks (up to 10 at a time) with task description, priority (High, Medium, Low), and due date.
- **View Tasks**: Display all tasks in a formatted table.
- **Delete Tasks**: Remove tasks by selecting their index from the list.
- **Update Tasks**: Modify the description, priority, or due date of existing tasks.
- **Search Tasks**: Search tasks based on their priority or due date.
- **CSV Storage**: Tasks are stored in a `task.csv` file for persistence.

## Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.x**
- `tabulate` library for table formatting

You can install the required `tabulate` library using the following command:

```bash
pip install tabulate
```
## How to Run the Application

1. Clone or download the repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Run the application using:

   ```bash
   python main.py
   ```
## Application Menu

Once the application starts, you will be presented with a main menu that looks like this:

-------MAIN MENU---------

1- Add task

2- View all tasks 

3- Delete task

4- Search a specific task 

5- Update task

6- Exit

You can select any of the options by entering the corresponding number.

## Usage Instructions

### 1. Add Task
- Choose option 1 from the main menu to add tasks.
- You can add up to 10 tasks at a time.
- For each task, provide:
  - Task description
  - Task priority (choose between High, Medium, or Low)
  - Task due date in YYYY-MM-DD format.

### 2. View All Tasks
- Choose option 2 to view all tasks stored in `task.csv`.
- Tasks will be displayed in a table with headers:
  - Task Description
  - Priority
  - Due Date

### 3. Delete Task
- Choose option 3 to delete a task.
- A list of tasks with their index numbers will be displayed.
- Enter the index number of the task you want to delete.

### 4. Search Task
- Choose option 4 to search for a specific task.
- You can search by:
  - Priority (High, Medium, Low)
  - Due date (YYYY-MM-DD format)

### 5. Update Task
- Choose option 5 to update an existing task.
- You can modify the:
  - Task description
  - Task priority
  - Due date
- Leave a field blank if you don't want to change it.

### 6. Exit Application
- Choose option 6 to exit the program.

## File Structure
The application has the following structure:

```bash
.
├── app_functions.py   # Contains all the task management functions
├── main.py            # The main entry point of the program
├── task.csv           # CSV file that stores task details
├── README.md          # This readme file
```
`task.csv`

This file is where all the tasks are stored in CSV format. Each task is stored with the following fields:

Task Description,Priority,Due Date

For example:

'Finish report,High,2024-09-12'

'Buy groceries,Medium,2024-09-15'

### Handling Errors
- If the `task.csv` file doesn't exist, it will be automatically created when you add a task.
- The application will notify you if you try to search for or delete tasks from an empty or non-existent file.
