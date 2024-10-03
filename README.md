# Expense Tracker

A simple command-line application to track your expenses. This tool allows you to add, edit, view, and save your expenses in a JSON file.

## Features

- Add new expenses with date, amount, and description.
- Edit existing expenses.
- View all expenses.
- Save expenses to a JSON file.

## Requirements

- Python 3.x
- Basic understanding of running Python scripts from the command line.

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rohitatzignuts/Expense-Tracker-In-Python.git
   cd expense-tracker
   ```

### Usage

1. Open your command line interface (CLI).
2. Navigate to the folder where the `index.py` file is located:

   ```bash
   cd path/to/your/folder
   ```

3. Run the script:
   ```bash
   python index.py
   ```

### How to Use

Once the program is running, you will see the following menu:

```
Expense Tracker
1 - Add Expense
2 - Edit Expense
3 - View Expenses
4 - Save and Exit
```

- **Add Expense**: You will be prompted to enter the date, amount, and description of the expense. You can skip the date to use the current date.
- **Edit Expense**: You can choose an existing expense by its ID to update its details.

- **View Expenses**: Display all the recorded expenses.

- **Save and Exit**: Save your expenses to a file and exit the program.

## File Format

Expenses are stored in a file named `expenses.json`. The format used is JSON, making it easy to read or modify manually if needed.
