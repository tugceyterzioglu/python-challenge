import pandas as pd

# load data from CSV file to pandas dataframe in python
file_path = '/Users/DataBootcamp/python-challenge/PyBank/resources/budget_data.csv'
data = pd.read_csv(file_path)

# total months
total_months = data['Date'].nunique()

# net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# changes in "Profit/Losses" over the entire period, and then the average of those changes
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()

# greatest increase in profits (date and amount) over the entire period
greatest_increase_in_profits = data.loc[data['Change'].idxmax()]

# greatest decrease in profits (date and amount) over the entire period
greatest_decrease_in_profits = data.loc[data['Change'].idxmin()]

#create the financial analysis
financial_analysis_text = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_in_profits['Date']} (${int(greatest_increase_in_profits['Change'])})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_in_profits['Date']} (${int(greatest_decrease_in_profits['Change'])})\n"   
)

# print financial analysis to terminal
print(financial_analysis_text)

#print financial analysis to text file
financial_analysis_file_path = '/Users/DataBootcamp/python-challenge/PyBank/analysis/financial_analysis.txt'
with open(financial_analysis_file_path, 'w') as file:
    file.write(financial_analysis_text)

print("Financial analysis complete. Results saved to financial_analysis.txt.")