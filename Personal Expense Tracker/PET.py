expenses = []

def add_expense(category,amount):
    expense = {
            category : amount
        }
    expenses.append(expense)
    print(f"{category}: {amount}")

def view_expenses():        
    if not expenses:
        print("Does Not Exist Expense")
    else:    
        for x in expenses:
            for category, amount in x.items():
                print(category, amount)

def search_expense(category):
    found = False
    for x in expenses:
        if category in x:
            print("This Expense is Exist.")
            found = True     
    if found == False:    
        print("Expense Does Not Exist.")

def delete_expense(category):
    found = False
    for x in expenses:
        if category in x:
            expenses.remove(x)
            print("Expense Delete Successfully")
            found = True
            break
    if found == False:
        print("Expense Does Not Exist")

def calculate_total():
    total = 0
    for x in expenses:
        for amount in x.values():
            total = total + amount
    print("The Total Expense is:", total)

def exit_program():
    print("Thank You💙")
    
print("======== Expense Tracker ========")
print("1. Add Expense")
print("2. View Expenses")
print("3. Search Expense")
print("4. Delete Expense")
print("5. Total Expenses")
print("6. Exit")

while True:
    try:
        choice = int(input("Enter Number:"))
    except ValueError:
        print("Enter a Number.")
        continue

    if choice == 1:
        category = input("Enter Name of Expense:")
        try:
            amount = int(input("Enter Amount of Expense:"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        add_expense(category,amount)

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        category = input("Enter Category :")
        search_expense(category)

    elif choice == 4:
        category = input("Enter Category:")
        delete_expense(category)

    elif choice == 5: 
        calculate_total()

    elif choice == 6:
        exit_program()
        break
        