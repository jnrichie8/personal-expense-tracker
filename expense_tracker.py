import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (food, travel, etc): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added!\n")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Expenses ---")
            for row in reader:
                print(f"Date: {row[0]} | Amount: £{row[1]} | Category: {row[2]}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")

def total_spent():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"\nTotal spent: £{total}\n")
    except FileNotFoundError:
        print("No expenses found.\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
