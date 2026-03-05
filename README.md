# Python To-Do List

A simple command-line To-Do List app built with Python.

This project lets you:
- Add tasks
- View tasks in a numbered list
- Remove tasks by number
- Exit the application

## What This Project Does

The app runs in a loop and asks for input from the user.  
Each task is stored in a Python list, displayed back to the user, and can be removed when needed.

## Python Methods Used

These are the main Python methods and built-ins used in `to-do.py`:

- `list.append(item)`  
Adds a new task to the end of `todo_items`.

- `enumerate(iterable, start=1)`  
Loops through tasks with index numbers starting from 1 for cleaner display.

- `str.strip()`  
Removes extra spaces before/after user input.

- `str.lower()`  
Converts menu input to lowercase so choices like `Add`, `ADD`, and `add` all work.

- `list.pop(index)`  
Removes a task by position and returns the removed item.

- `len(list)`  
Checks if the task number entered is within a valid range.

- `int(value)`  
Converts the entered task number from string to integer.

## Python Concepts Learned

This project demonstrates:

- Functions  
Defined a `main()` function to organize program logic.

- Lists  
Used a list to store and manage dynamic to-do items.

- Loops  
Used `while True` for repeated interaction until user exits.  
Used a `for` loop to display each task.

- Conditionals  
Used `if`, `elif`, and `else` to handle user choices (`add`, `remove`, `exit`).

- Input and Output  
Used `input()` to collect user data.  
Used `print()` to show prompts, lists, and status messages.

- Error Handling  
Used `try/except ValueError` to prevent crashes when non-numeric input is entered for task removal.

- String Formatting  
Used f-strings like `f"{index}. {item}"` for readable output.

## How To Run

1. Make sure Python is installed.
2. Run the script:

```bash
python to-do.py