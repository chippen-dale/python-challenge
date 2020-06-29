import os
import csv

#Lists for reference
month_to_month= []
month_year = []

#Initialized variables
count = 0
updated_profit = 0
initial_balance = 0


with open('Resources/budget_data.csv') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:    
    # Used for capturing Month / Year in relation to increase/decrese in profits
        month_year.append(row[0])
        
    #Update profit when reading each row
        updated_profit = updated_profit + int(row[1])

    #Calculate the average change from month to month. Then calculate the difference
        final_balance = int(row[1])            
        monthly_change = final_balance - initial_balance
        
    #Capture Monthly Changes and store them.  Start each iteration with previous balance
        month_to_month.append(monthly_change)
        initial_balance = final_balance

    #Greatest Increase and Greatest Decrease and their Mo/Year
        greatest_increase_profits = max(month_to_month)
        greatest_decrease_profits = min(month_to_month)
        max_increase_mo_yr = month_year[month_to_month.index(greatest_increase_profits)]
        max_decrease_mo_yr = month_year[month_to_month.index(greatest_decrease_profits)]
    #Increment Count
        count +=1
    #Calculate Average Change - Assumption (initial balance is counted as a change)
        average_change_profits = (sum(month_to_month)/count)        
            
    x = str("--------------------------------------------------")   
    print(x)
    print("Financial Analysis")
    print(x)
    print("Total Months:    " + str(count))
    print("Total Profits:   " + "$" + str(updated_profit))
    print("Average Change:  " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(max_increase_mo_yr) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(max_decrease_mo_yr) + " ($" + str(greatest_decrease_profits)+ ")")
    print(x)
    
financial_analysis = os.path.join("Analysis", "financial_analysis.txt")
with open(financial_analysis, "w") as outfile:
    outfile.write("--------------------------------------------------\n")
    outfile.write("Financial Analysis\n")
    outfile.write("--------------------------------------------------\n")
    outfile.write("    Total Months: " + str(count) + "\n")
    outfile.write("    Total Profits: " + "$" + str(updated_profit) +"\n")
    outfile.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    outfile.write("    Greatest Increase in Profits: " + str(max_increase_mo_yr) + " ($" + str(greatest_increase_profits) + ")\n")
    outfile.write("    Greatest Decrease in Profits: " + str(max_decrease_mo_yr) + " ($" + str(greatest_decrease_profits) + ")\n")
