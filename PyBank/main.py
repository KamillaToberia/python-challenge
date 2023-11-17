#Import the os module, this will allow us to create file paths across operating systems:
import os

#Reading CSV files:
import csv

# Variables
profit=[]
monthly_changes=[]
date=[]
count=0
total_profit=0
total_change_profits=0
initial_profit=0

#Copy the relative path PyBank\Resources\budget_data.csv
budget_data_csv=os.path.join("PyBank/Resources/budget_data.csv")

#Reading in the CSV file
with open(budget_data_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    #Skip the header
    csv_header=next(csv_reader)
    print(f"CSV Header:{csv_header}") #to see the header
   
    #Read each row of data after the header
    for row in csv_reader:
    #print(row)
 
        #Calculating the total of months included in the dataset
        count=count+1
    
        #To collect the greatest increase and decrease profits
        date.append(row[0])
        
        #Total amount of profit    
        profit.append(row[1])
        total_profit= total_profit+int(row[1])

        #Calculate the average month to mont. Then Calculate the average change
        final_profit=int(row[1])
        monthly_change_profits=final_profit-initial_profit

        #Store these monthly changes
        monthly_changes.append(monthly_change_profits)
        total_change_profits=total_change_profits+monthly_change_profits
        initial_profit=final_profit

        #Calculate the average change in profits
        average_change_profits=((total_change_profits/count)*-2)
        
        #Max Profit/Losses and Min Profit/Losses
        increase_profits=max(monthly_changes)
        decrease_profits=min(monthly_changes)

        increase_date=date[monthly_changes.index(increase_profits)]
        decrease_date=date[monthly_changes.index(decrease_profits)]
       
        # Print the analysis
    print("-------------------------------------------------------------")
    print("Financial Analysis")
    print("-------------------------------------------------------------")
    print(f"Total Months:  {count}")
    print(f"Total:  ${total_profit}")
    print(f"Average Change:  ${average_change_profits:.2f}")
    print(f"Greatest Increase in Profits:  {increase_date}  (${increase_profits})")
    print(f"Greastest Decrease in Losses:  {decrease_date}  (${decrease_profits})")
    print("--------------------------------------------------------------")

    #Export a text file with the results
    
    with open("financial_analysis.txt","w") as outfile:
    
        outfile.write("-------------------------------------------------------\n")
        outfile.write("Financial Analysis\n")
        outfile.write("-------------------------------------------------------\n")
        outfile.write(f"Total Months:  {count}\n")
        outfile.write(f"Total:  ${total_profit}\n")
        outfile.write(f"Average Change:  ${average_change_profits:.2f}\n")
        outfile.write(f"Greatest Increase in Profits:  {increase_date} (${increase_profits})\n")
        outfile.write(f"Greatest Decrease in Losses:  {decrease_date} (${decrease_profits})\n")
        outfile.write("--------------------------------------------------------\n")
