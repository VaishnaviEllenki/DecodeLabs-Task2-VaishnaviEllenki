import csv
import os

FILENAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense Added Successfully!")


def view_expenses():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n===== EXPENSE LIST =====")
        for row in reader:
            print(
                f"Date: {row[0]} | Category: {row[1]} | ₹{row[2]} | {row[3]}"
            )


def total_expense():
    total = 0

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[2])

    print(f"\n💰 Total Expense: ₹{total}")


def search_category():
    category = input("Enter category to search: ")

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        found = False

        for row in reader:
            if row[1].lower() == category.lower():
                found = True
                print(
                    f"Date: {row[0]} | ₹{row[2]} | {row[3]}"
                )

        if not found:
            print("❌ No expenses found.")


def delete_expense():
    date = input("Enter date of expense to delete: ")

    rows = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] != date:
                rows.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("✅ Expense Deleted!")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_category()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("❌ Invalid Choice!")