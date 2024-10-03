---

# Expense Tracker

A simple command-line application to track your expenses. This tool allows you to add, edit, view, and delete your expenses stored in a MySQL database.

## Features

- Add new expenses with date, amount, and description.
- Edit existing expenses.
- View all expenses.
- Delete an expense.
- Save expenses directly to a MySQL database.

## Requirements

- Python 3.x
- MySQL server running and accessible
- `mysql-connector-python` library installed

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rohitatzignuts/Expense-Tracker-In-Python.git
   cd expense-tracker
   ```

2. **Install the required library**:

   ```bash
   pip install mysql-connector-python
   ```

### Database Setup

1. **Create a MySQL database**:

   ```sql
   CREATE DATABASE `expense-tracker`;
   ```

2. **Create a table for expenses**:

   ```sql
   USE `expense-tracker`;

   CREATE TABLE `expenses` (
       `id` INT AUTO_INCREMENT PRIMARY KEY,
       `date` DATE,
       `amount` INT,
       `description` VARCHAR(255)
   );
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
4 - Delete Expenses
5 - Save and Exit
```

- **Add Expense**: You will be prompted to enter the date, amount, and description of the expense. You can skip the date to use the current date.
- **Edit Expense**: You can choose an existing expense by its ID to update its details.
- **View Expenses**: Display all the recorded expenses.
- **Delete Expenses**: You can choose an expense by its ID to delete.
- **Save and Exit**: All expenses are automatically saved to the MySQL database upon exit.

## Database Structure

Expenses are stored in a MySQL database named `expense-tracker`, specifically in the `expenses` table, with the following structure:

| Column        | Type         | Description                  |
| ------------- | ------------ | ---------------------------- |
| `id`          | INT          | Auto-incrementing identifier |
| `date`        | DATE         | Date of the expense          |
| `amount`      | INT          | Amount of the expense        |
| `description` | VARCHAR(255) | Description of the expense   |

---
