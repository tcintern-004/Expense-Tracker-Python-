# Command-Line Expense Tracker

A simple Python command-line application that allows users to manage their daily expenses. The project demonstrates the use of Python fundamentals such as functions, lists, dictionaries, loops, exception handling, file handling, and JSON serialization while providing a practical real-world application.

## Project Overview

Managing expenses is a common task, and this application provides a lightweight solution that runs entirely in the terminal. Users can add, view, delete, search, and summarize expenses. All data is stored in a JSON file so that expenses persist even after the program is closed.

## Features

* Add a new expense
* View all recorded expenses
* Delete an expense by ID
* Calculate total expenses
* Search expenses by category
* Display an expense summary
* Save data to a JSON file
* Automatically load saved expenses when the application starts
* Gracefully handle invalid user input

## Technologies Used

* Python 3
* JSON Module

## Data Structure

The application stores expenses as a list of dictionaries.

**Example:**
```json
[
    {
        "id": 1,
        "category": "Food",
        "description": "Burger",
        "amount": 500
    },
    {
        "id": 2,
        "category": "Transport",
        "description": "Bus Ticket",
        "amount": 80
    }
]
```

### Data Structure Choices

**Why a List?**  
Lists are used because they preserve insertion order and allow easy iteration over multiple expense records while mapping perfectly to JSON arrays.

**Why Dictionaries?**  
Dictionaries allow accessing expense attributes (like ID and amount) via readable keys, making `expense["category"]` much clearer than an index like `expense[1]`.

### Why JSON?
Instead of storing data in a text file, JSON was chosen because:
* It is human-readable.
* Python provides built-in support using the `json` module.
* It easily stores complex structures like lists and dictionaries.
* Data persists between program executions.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tcintern-013/expense-tracker.git](https://github.com/tcintern-013/expense-tracker.git)
   ```
2. **Move into the project directory:**
   cd expense-tracker

3. **Run the program:**
   python main.py
   
## Run It Live (GitHub Codespaces)

You can run this project instantly in your browser — no local Python setup needed — using GitHub Codespaces.

1. Open this repository on GitHub.
2. Click the green **<> Code** button (top right of the file list).
3. Switch to the **Codespaces** tab.
4. Click **Create codespace on main**.
5. Wait a few seconds for the browser-based VS Code environment to load — the whole repo will already be there.
6. Open a terminal inside Codespaces: **Terminal → New Terminal** (or press ``Ctrl + ` ``).
7. Run the app:
   ```bash
   python main.py
   ```
   
## Python Concepts Demonstrated
*Functions
*Lists
*Dictionaries
*Loops
*Conditional Statements
*Exception Handling
*JSON File Handling
*User Input Validation
*Modular Programming

## Author
Abdul Hadi

This project was developed as a Python programming exercise to practice file handling, data structures, and building 
an interactive command-line application.




