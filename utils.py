from datetime import datetime


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_category():
    while True:
        category = input("Enter category (Food/Travel/Shopping/Other): ")
        category = category.strip().title()

        if category:
            return category

        print("Category cannot be empty.")


def get_date():
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text

        except ValueError:
            print("Invalid date. Example: 2026-10-03")


def get_description():
    while True:
        description = input("Enter description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")