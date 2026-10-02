from src.expense import Expense
from src.file_manager import load_expenses, save_expenses
from src.utils import (
    get_amount,
    get_category,
    get_date,
    get_description
)


def add_expense(expenses):
    print("\n========== ADD NEW EXPENSE ==========")

    amount = get_amount()
    category = get_category()
    date = get_date()
    description = get_description()

    expense = Expense(
        amount,
        category,
        date,
        description
    )

    expenses.append(expense)

    if save_expenses(expenses):
        print("\n✅ Expense added successfully!")
    else:
        expenses.pop()
        print("\n❌ Expense could not be saved.")


def view_expenses(expenses):
    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense}")

    total = sum(expense.amount for expense in expenses)

    print("----------------------------------")
    print(f"Total Expenses: ₹{total:.2f}")


def main():
    # Load previously saved expenses
    expenses = load_expenses()

    while True:

        print("\n========================================")
        print("       PERSONAL FINANCE MANAGER")
        print("========================================")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice (1-3): ").strip()2
        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("\nThank you for using Personal Finance Manager!")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")


# Start the program
if __name__ == "__main__":
    main()