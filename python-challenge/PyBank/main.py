#Step 0: Import the csv file
import csv
import os   # needed for exporting the txt file of the analysis.  import os constructs paths dynamically, check file existence, list or navigate directories, and change the working directory.

# Step 1: Define the path to your CSV file
file_path = r'C:\Users\devin\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv' # Add "r" in front of the path because it tells pyton to interpret the raw string literally. This is due to (/) being treated as literal characters instead of escape characters.

# Step 2: Initialize variables
total_months = 0        # 0 for integers, since counting starts with 0.
net_total = 0       
previous_profit = None      # Used to calculate the change in profit/loss between consecutive months. Is set to 'none' because the in the first row of data there isn't any values present, and 'none' will allow the program to take this into account to prevent errors.
changes = []        # [] is used to create an empty list to store values calculated during the loop.
greatest_increase = {"date": None, "amount": float('-inf')}     # Set to -inf to ensure any number compared to -inf will be larger, which will ensure the first value encountered in the loop will be the new 'greatest increase'. Using 0 could cause an error due to the first changes in profits being below 0.
greatest_decrease = {"date": None, "amount": float('inf')}      # 'Float' is a data type used to represent numbers with a decimal point/fractional values. 'Int' will only read whole numbers.

# Step 3: Read the CSV file
with open(file_path, 'r') as csvfile:       # 'With' is used when opening files that need to be managed and properly closed after use. // 'r' stands for read mode, which is used when you want to open a file for reading only.
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date = row[0]       
        profit = int(row[1])        # Translates to: 'In this row, take the value from the second column and interpret it as an integer.'
        
        # Update total months and net total counter
        total_months += 1       # Tells the counter to go to the next month.
        net_total += profit     # Net_total starts at 0. Value of 'profit' added to net_total during each iteration.  '+= adds the current profit to the running total.

        # Calculate monthly change
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)      # append() adds the calculated change in profit/loss from one month to the next, and adds it to the next in a list called changes.
            
            # Check for greatest increase/decrease
            if change > greatest_increase["amount"]:        # 'Amount' is a key (a string that acts as a label for a value in the dictionary), and will work so long as you reference the same key consistently.
                greatest_increase = {"date": date, "amount": change}
            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}

        # Update previous profit
        previous_profit = profit        # Not clear on how this works but is necessary for updating the profit of consecutive months.

# Step 4: Calculate average change
average_change = sum(changes) / len(changes) if changes else 0      # len() returns the number of items in an object.  Here, it is calculating the number of elements in the list.

# Step 5: Format the results
analysis_results = (
    "Financial Analysis\n"      # \n inserts a new line in the string. 
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

# Step 6: Print the analysis
print(analysis_results)

# Step 7: Export analysis to specific folder
output_folder = r'C:\Users\devin\OneDrive\Desktop\python-challenge\PyBank\analysis'

if not os.path.exists(output_folder):       # Makes a folder if one does not exist yet.
    os.makedirs(output_folder) 

output_file = os.path.join(output_folder, 'pyBank_analysis.txt')

with open(output_file, 'w') as file:
    file.write(analysis_results)

print(f'analysis_results exported to: {output_file}')