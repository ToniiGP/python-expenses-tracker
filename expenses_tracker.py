import re #importing regular expressions module 
import json #importing module to work with json files in data handling 

#Defining Functions 


#Function to save data as a json file 
def save_expenses(expenses, filename="expenses.json"):
    try:
        with open(filename, "w") as file:
            json.dump(expenses,file,indent=4)
        print(f"✅ Expenses saved to {filename}")
    except:
        print(f"❌ Error saving expenses")
        
        
        
#Function to load date from json file 
def load_expenses(filename = "expenses.json"):
    try: 
        with open (filename, "r") as file:
            expenses = json.load(file)
            print(f"✅ Expenses loaded from {filename}")
        return expenses
    except FileNotFoundError:
        print(f"ℹ️ No saved file found, starting fresh.")
        return []
    except json.JSONDecodeError:
        print("❌ JSON file is corrupted or malformed.")
        return []



#creating function that creates the expenses 'board' 
def expenses_board(): 
    expenses = [] #creating list to save the expenses 
    while True:  #using a loop to store multiple data 
         print("----------------------------------------")
         
        #getting input from the user
         while True:
            category = input("Please Insert the expense category: ").strip()
            #making sure category is not empty 
            if category:
                break
            print("Category can not be empty")
            
            
         while True:
            amount_input = input("Please Insert the expense amount: $")
            #adding input validation to make sure amount is a number/float 
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("Please enter a valid number")
                
             
         while True: 
            date = input("Please Insert the date of expense(YYYY-MM-DD): ")
            #adding input validation to make sure the date is in the right format 
            if re.match(r"\d{4}-\d{2}-\d{2}", date):
                break
            else:
                print("Please enter a valid date (YYYY-MM-DD)")
                
                
         while True:
            note = input("Expense Note: ").strip()
            #making sure note is not empty
            if note:
                break
            print("Note can not be empty")
            
         
         #Storing as a dictionary 
         expense = {
             "category": category,
             "amount": amount,
             "date": date, 
             "note": note     
         }
         
         
         expenses.append(expense) #adding dictionaries (expenses) to a list 
         answer = input("Is this the last expense? (yes/no): ").strip().lower() 
         if answer == "yes" : 
             break 
         
    return expenses 



#Creating Function to save expenses per month 
def monthly_expenses(expenses):
    #Creating Dictionary to store the monthly expenses 
    monthly_groups = {}
    month_names = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    #accesing needed information with a for loop 
    for g in expenses: 
        match = re.search(r"\d{4}-(\d{2})-\d{2}", g["date"]) #created a regular expression to get the month of the expense from the date
        if match:
            month_number = match.group(1)    #adding the expense to it's month in 
            month = month_names.get(month_number, "Unknown")
            
            if month not in  monthly_groups:
                monthly_groups[month] = []
            
            monthly_groups[month].append(g)
            
        else:
            print(f"Could not parse date for expense: {g}")
        
    #Print The Grouped Expenses: 
    for month, items in monthly_groups.items():
        print(f"\nExpenses for {month}: ")
        print("-" * 20)
        total = 0
        for item in items:
            print(item)
            try:
                total+= float(item.get("amount", 0))
            except ValueError:
                print("All date must be numbers")
        print(f"Total spent in {month} is: ${total:.2f}")
    
    #Getting Grand Total: 
    grand_total = 0 
    for items in monthly_groups.values():
        for item in items:
            try:
                grand_total += float(item.get("amount", 0))
            except ValueError:
                print("All data must be numbers")
    
    print("\n" + "=" * 20)
    print(f"💰 Grand Total Spent: ${grand_total:.2f}")
    print("=" * 20)
            
        
        
        
#Main Program 
print("📊 Welcome to Expenses Tracker")

#Load existing expenses
all_expenses = load_expenses()

#Input new expenses
new_expenses = expenses_board()

#add new expenses the the full list
all_expenses.extend(new_expenses)

#Save updated list to file
save_expenses(all_expenses)

#Display monthly report 
monthly_expenses(all_expenses)
