def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        print("4. Filter by Category")

        choice = input("Choose option: ")

        if choice == "1":
            category = input("Category: ")
            item = input("Item: ")
            amount = input("Amount: ")
            add_expense(category, item, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        elif choice == "4":
            category = input("Filter by category: ")
            filter_by_category(category)

def add_expense(category, item, amount):
    with open("expense.txt", "a") as f:
        f.write(f"{category},{item},{amount}\n")

def view_expenses():
    total = 0
    with open("expense.txt", "r") as f:
        try:
            for line in f:
                print(line.strip())
                parts = line.strip().split(",")
                total += int(parts[2])
        except ValueError:
            print("Invalid data in file!")
    print(f"Total: {total}")

def filter_by_category(category):
    with open("expense.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0].lower() == category.lower():
                print(line.strip())

menu()