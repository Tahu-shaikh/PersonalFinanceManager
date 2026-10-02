import csv
from pathlib import Path

from src.expense import Expense


# Location of our CSV file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.csv"

# Column names in CSV file
HEADERS = ["Amount", "Category", "Date", "Description"]


def save_expenses(expenses):
    try:
        # Create data folder if it does not exist
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        # Open CSV file for writing
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Write column headings
            writer.writerow(HEADERS)

            # Write each expense
            for expense in expenses:
                writer.writerow([
                    expense.amount,
                    expense.category,
                    expense.date,
                    expense.description
                ])

        return True

    except OSError as error:
        print(f"Error saving expenses: {error}")
        return False


def load_expenses():
    try:
        # Create data folder if it does not exist
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        # If CSV doesn't exist, create an empty one
        if not DATA_FILE.exists():
            save_expenses([])
            return []

        expenses = []

        # Open CSV file for reading
        with DATA_FILE.open("r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            # Read every expense
            for row in reader:
                try:
                    expense = Expense(
                        row["Amount"],
                        row["Category"],
                        row["Date"],
                        row["Description"]
                    )

                    expenses.append(expense)

                except (ValueError, KeyError, TypeError):
                    print("Warning: Invalid expense found in CSV.")

        return expenses

    except OSError as error:
        print(f"Error reading expenses: {error}")
        return []