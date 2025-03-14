from datetime import datetime as dt
from tkinter import *

class Expense:
    def __init__(self, name, category, amount, date):
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date
        
    def __str__(self):
        return f"{self.name}, {self.category}, {self.amount}, {self.date}\n"
            
def get_income():
    print("Getting user income")
    monthly_income = float(input("Enter your net monthly income: "))
    return monthly_income
    
def get_expense():
    print("Getting user expense...")
    expense_name = input("Enter expense name: ")
    expense_category = input("Enter expense category: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_date = input(f"Enter expense date (mm/dd/yyyy): ")
    formatted_expense_date = dt.strptime(expense_date, '%m/%d/%Y')   # format date for storage
    
    # Instantiate expense object and return
    return Expense(expense_name, expense_category, expense_amount, formatted_expense_date)

def save_expense_to_CSV_file(expense, filename):
    print("Saving to CSV...")

    with open(filename, "a") as file:
        file.write(str(expense))
        
    file.close()
    
def sum_expenses(filename, income):
    print("Summing expenses...")
    
    # Open csv file to read and sum amounts line by line
    with open(filename, "r") as file:
        total_expenses = 0
        for row in file:
            line = row.split(',')
            total_expenses += float(line[2])
        print(f"Total expenses this month are {total_expenses}")
        
    file.close()
    
    return total_expenses
        
def calculate_remaining_income(monthly_income, total_expenses):
    print("Calculating remaining income...")
    remaining_income = monthly_income - total_expenses
    print(f"Total money remaining for the month is {remaining_income}")
        
    # Future functionality - check remaining against predefined budget/savings percentage
    def calculate_remaining_as_percentage():
        pass
    
    # if calculate_percentage:
    #   calculate_remaining_as_percentage()
    
    

def main():
    print(f"Running Expense Tracker!")
    
    # Input monthly income
    income = get_income()
    
    # Get user to input expense
    #expense = get_expense()
    
    # Write expense to CSV file
    filename = "expenses.csv"
    #save_expense_to_CSV_file(expense, filename)
    
    # Read file and sum expenses
    expenses = sum_expenses(filename, income)
    
    # Calculate remaining income 
    calculate_remaining_income(income, expenses)

if __name__ == "__main__":
    main()