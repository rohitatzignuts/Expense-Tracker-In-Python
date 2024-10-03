import datetime
import json
import random


# Get Expenses
def get_expenses(file="expenses.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON")
        return []


# Save Expenses
def save_expenses(data, file="expenses.json"):
    try:
        with open(file, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error while saving: {e}")


# Add Expense
def add_expense(expenses):
    try:
        date = input("Enter Date (DD-MM-YYYY) or skip: ")
        amount = input("Enter Amount: ")
        description = input("Enter Description: ")

        # format date
        if date:
            try:
                date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%d-%m-%Y")
            except ValueError:
                print("Invalid Date Value!!")
                return
        else:
            date = datetime.datetime.now().strftime("%d-%m-%Y")

        # format amount
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid Amount Value!!")
            return

        expense = {
            "id": random.randint(1, 1000),
            "date": date,
            "amount": amount,
            "description": description,
        }

        # append expense
        expenses.append(expense)
        print("Expense added!")
    except Exception as e:
        print(f"Error adding an expense: {e}")


# Edit Expense
def edit_expense(expenses):
    view_expenses(expenses)
    try:
        edit_id = int(input("Select Id for the expense to be edited: "))
    except ValueError:
        print("Invalid ID")
        return

    for expense in expenses:
        if expense["id"] == edit_id:
            return expense
    print("Expense not found.")
    return


# View Expenses
def view_expenses(expenses):
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


# Delete Expenses
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        del_id = int(input("Select Id for the expense to be deleted: "))
    except ValueError:
        print("Invalid ID")
        return

    # Create a new list without the expense to be deleted
    updated_expenses = [expense for expense in expenses if expense["id"] != del_id]

    if len(updated_expenses) < len(expenses):
        expenses[:] = updated_expenses
        save_expenses(expenses)
        print("Expense Deleted!!")
    else:
        print("Expense not found.")

    return


def main():
    expenses = get_expenses()

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
            add_expense(expenses)
        elif choice == "2":
            res = edit_expense(expenses)
            if res:
                date = input(f"Date (DD-MM-YYYY) [{res['date']}]: ")
                if date:
                    res["date"] = datetime.datetime.strptime(date, "%d-%m-%Y").strftime(
                        "%d-%m-%Y"
                    )

                amount = input(f"Amount [{res['amount']}]: ")
                if amount:
                    try:
                        res["amount"] = float(amount)
                    except ValueError:
                        print("Invalid amount")

                description = input(f"Description [{res['description']}]: ")
                if description:
                    res["description"] = description

                print("Expense updated!!")
        elif choice == "3":
            view_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            save_expenses(expenses)
            break
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    main()
