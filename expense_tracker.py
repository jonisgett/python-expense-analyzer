from datetime import datetime

# Create a class for an Expense
class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"""Amount: ${self.amount:.2f}
Category: {self.category}
Description: {self.description}
Date: {self.date}"""
    
# Create a class that defines Tracking Expenses
class ExpenseTracker:
    # constructor
    def __init__(self):
        self.expenses = [] # list to old all the Expense objects
    # method for adding an expense
    def add_expense(self, expense):
        self.expenses.append(expense)
    # method for deleting an expense
    def remove_expense(self, expense):
        self.expenses.remove(expense)
    # method for viewing a list of current expenses
    def view_expenses_numbered_sorted(self):
        if not self.expenses:
            print("No expenses yet!\n")
            return []
        else:
            sorted_expenses = sorted(self.expenses, key=lambda x: x.date, reverse=True)
            print("===Expense List===")
            for i, expense in enumerate(sorted_expenses, start=1):
                print(f"\n{i}:")
                print(f"{expense}")
                print()
        return sorted_expenses
    # method for loading expenses from a json file
    def load_expenses(self):
        pass
    # method for saving expenses to a json file
    def save_expenses(self):
        pass

# Create/Show User Menu
def show_menu():
    print("===Expense Tracker===")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Quit")
    print("=====================")

def get_menu_choice():
    # Get menu choice from user
    while True:
        choice = input("Please choose a number from the menu: ")
        try:
            choice_int = int(choice)
            if choice_int in range(1, 5):
                break
            else: 
                print("Invalid input. The number you chose is not on the menu!")
        except ValueError:
            print("Invalid input. Please choose a number from the menu")
    return choice_int

# Get the number of the expense the user wants to delete
def get_expense_to_delete(expenses):
    while True:
        user_input_number = input("Please choose the number of an expense to delete: ")
        try:
            parsed_user_input = int(user_input_number)
            if parsed_user_input in range(1, len(expenses) + 1):
                break
            else:
                print("Invalid input. Number not in range.")
        except ValueError:
            print("Invalid input. Please choose a number.")
    expense_to_delete = expenses[parsed_user_input-1]
    return expense_to_delete
# Get new expense data from user
def get_expense_info():
    # Get and validate an amount from the user
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount > 0:
                break
            else:
                print(f"Invalid input.  The amount you enter must be positive!")
        except ValueError:
            print("Invalid input. Please enter a valid monetary amount!")
    # Get the Category of the expense from the user
    category = input("Category: ").strip()
    if not category:
        category = "Unknown"
    
    # Get the Description of the expense from the user
    description = input("Description: ").strip()
    if not description:
        description = "Unknown"

    # Get the date from the user
    date_input = input("Date (YYYY-MM-DD) or Enter for today: ")
    if date_input == "":
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            parsed_date = datetime.strptime(date_input, '%Y-%m-%d')
            date = parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid Date. Using today's date.")
            date = datetime.today().strftime('%Y-%m-%d')
    return Expense(amount, category, description, date)

def main():
    # Create new Expense instance
    tracker = ExpenseTracker()

    while True:
        # Show menu
        show_menu()
        # Get menu choice from user
        user_menu_choice = get_menu_choice()
        # now we need to check what number the user chose and do appropriately
        if user_menu_choice == 1:
            tracker.view_expenses_numbered_sorted()
        elif user_menu_choice == 2:
            expense = get_expense_info()
            tracker.add_expense(expense)
        elif user_menu_choice == 3:
            # view and return sorted list for possible deletion
            sorted_expenses = tracker.view_expenses_numbered_sorted()
            # if no expenses yet let the user know they can't delete
            if sorted_expenses:
                expense_to_delete = get_expense_to_delete(sorted_expenses)
                tracker.remove_expense(expense_to_delete)
            else:
                print("No expenses yet!")
        elif user_menu_choice == 4:
            print("Goodbye!")
            break


  

if __name__ == "__main__":
    # call main
    main()
    
    


