import datetime
import random
from dbtest import my_cursor, mydb


# Get Expenses
def getExpenses():
    try:
        my_cursor.execute("SELECT * FROM `expenses`")
        results = my_cursor.fetchall()

        # Convert the results into a list of dictionaries
        expenses = []
        for row in results:
            expenses.append(
                {"id": row[0], "date": row[1], "amount": row[2], "description": row[3]}
            )

        return expenses
    except Exception as e:
        print(f"Error getting Expenses from DB: {e}")
        return []


# Save Expense
def saveExpenses(expense):
    try:
        sql = "INSERT INTO `expenses` (date, amount, description) VALUES (%s, %s, %s)"
        val = (expense["date"], expense["amount"], expense["description"])
        my_cursor.execute(sql, val)
        mydb.commit()
        print("Expense added to the database!")
    except Exception as e:
        print(f"Error while adding expense to the DB: {e}")


# Add Expense
def addExpense():
    try:
        date = input("Enter Date (DD-MM-YYYY) or skip: ")
        amount = input("Enter Amount: ")
        description = input("Enter Description: ")

        # Format date
        if date:
            try:
                date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid Date Value!!")
                return
        else:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Format amount
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid Amount Value!!")
            return

        expense = {
            "date": date,
            "amount": amount,
            "description": description,
        }

        # Save the expense to the DB
        saveExpenses(expense)
        print("Expense added!")
    except Exception as e:
        print(f"Error adding an expense: {e}")


# Edit Expense
def editExpenses():
    expenses = getExpenses()
    viewExpenses()

    try:
        edit_id = int(input("Enter ID for the expense to be edited: "))
        expense = next((e for e in expenses if e["id"] == edit_id), None)

        if not expense:
            print("Expense not found.")
            return

        # Update date, amount, and description
        new_date = input(f"Date (DD-MM-YYYY) [{expense['date']}]: ")
        expense["date"] = new_date if new_date else expense["date"]

        # Ensure amount is a float, handling invalid input
        new_amount = input(f"Amount [{expense['amount']}]: ")
        expense["amount"] = float(new_amount) if new_amount else expense["amount"]

        new_description = input(f"Description [{expense['description']}]: ")
        expense["description"] = (
            new_description if new_description else expense["description"]
        )

        # Convert the date to the correct format if it was updated
        if new_date:
            expense["date"] = datetime.datetime.strptime(
                expense["date"], "%d-%m-%Y"
            ).strftime("%Y-%m-%d")

        # Update the expense in the database
        sql = "UPDATE `expenses` SET date = %s, amount = %s, description = %s WHERE id = %s"
        my_cursor.execute(
            sql, (expense["date"], expense["amount"], expense["description"], edit_id)
        )
        mydb.commit()
        print("Expense updated!!")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"Error updating expense: {e}")


# View Expenses
def viewExpenses():
    expenses = getExpenses()
    if not expenses:
        print("Nothing to show...")
        return
    else:
        print("----------------")
        for expense in expenses:
            print(
                f"{expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}, Id: {expense['id']}"
            )
        print("----------------")


# View Expenses
def deleteExpense():
    expenses = getExpenses()
    viewExpenses()

    try:
        del_id = int(input("Enter ID for the expense to be deleted: "))

        sql = "DELETE FROM `expenses` WHERE id = %s"
        my_cursor.execute(sql, (del_id,))
        mydb.commit()

        print("Expense Deleted!!")
    except ValueError:
        print("Invalid ID.")
    except Exception as e:
        print(f"Error deleting expense: {e}")


def main():

    while True:
        print("\n")
        print("Expense Tracker")
        print("1 - Add Expense")
        print("2 - Edit Expense")
        print("3 - View Expenses")
        print("4 - Delete Expense")
        print("5 - Save and Exit")
        print("\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            addExpense()
        elif choice == "2":
            editExpenses()
        elif choice == "3":
            viewExpenses()
        elif choice == "4":
            deleteExpense()
        elif choice == "5":
            break
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    main()
