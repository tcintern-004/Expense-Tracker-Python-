import json
import os
from datetime import datetime

FILE_NAME = 'expenses.json'

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nError reading data file. Starting with an empty tracker.")
        return []

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    print("\n Add New Expense ")
    
    while True:
        try:
            amount = float(input("Amount ($): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    category = input("Category (e.g., Food, Transport, Utilities): ").strip().title()
    description = input("Description: ").strip()
    date_str = datetime.now().strftime("%Y-%m-%d")

    new_id = 1 if not expenses else max(exp.get('id', 0) for exp in expenses) + 1

    expense = {
        "id": new_id,
        "date": date_str,
        "amount": amount,
        "category": category if category else "Uncategorized",
        "description": description if description else "N/A"
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nSuccessfully added: ${amount:.2f} for {expense['category']}.")

def view_expenses(expenses, filtered_list=None):
    target_list = filtered_list if filtered_list is not None else expenses
    
    if not target_list:
        print("\nNo expenses found.")
        return

    print("\n" )
    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 70)
    for exp in target_list:
        print(f"{exp['id']:<5} | {exp['date']:<12} | {exp['category']:<15} | ${exp['amount']:<9.2f} | {exp['description']}")
    print("\n")

def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses to delete.")
        return
        
    view_expenses(expenses)
    
    try:
        exp_id = int(input("\nEnter the ID of the expense to delete (or 0 to cancel): "))
        if exp_id == 0:
            return
            
        for i, exp in enumerate(expenses):
            if exp['id'] == exp_id:
                deleted = expenses.pop(i)
                save_expenses(expenses)
                print(f"\nDeleted expense ID {exp_id} (${deleted['amount']:.2f} for {deleted['category']}).")
                return
                
        print("\nExpense ID not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid numerical ID.")

def calculate_total(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def search_by_category(expenses):
    category = input("\nEnter category to search for: ").strip().title()
    filtered = [exp for exp in expenses if exp['category'] == category]
    
    if filtered:
        print(f"\n Search Results for {category}")
        view_expenses(expenses, filtered)
        total = sum(exp['amount'] for exp in filtered)
        print(f"Total for {category}: ${total:.2f}")
    else:
        print(f"\nNo expenses found in the '{category}' category.")

def summary_by_category(expenses):
    if not expenses:
        print("\nNo expenses to summarize.")
        return
        
    summary = {}
    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']
        
    print("\nExpense Summary by Category")
    print(f"{'Category':<20} | {'Total Amount'}")
    print("\n")
    for cat, total in sorted(summary.items(), key=lambda item: item[1], reverse=True):
        print(f"{cat:<20} | ${total:.2f}")
    print("\n")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n" + "="*30)
        print("PYTHON EXPENSE TRACKER")
        print("="*30)
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Calculate total expenses")
        print("5. Search by category")
        print("6. Summary by category")
        print("7. Exit")
        print("="*30)
        
        choice = input("Select an option (1-7): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            calculate_total(expenses)
        elif choice == '5':
            search_by_category(expenses)
        elif choice == '6':
            summary_by_category(expenses)
        elif choice == '7':
            print("\nSaving data and exiting.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()