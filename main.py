import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

with open(csvpath, 'r') as csvfile:   #Reading the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Date=[]
    Profit_Losses=[]
    Net_Total=0
    Total=0
    Change=0
    Total_Change=0
    Avg_Change=0
    Greatest_Increase_Date=""
    Greatest_Decrease_Date=""

    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))

    Greatest_Increase = Profit_Losses[1]- Profit_Losses[0]   #This calculate the greatest increase in the profit/losses  over the entire period

    Greatest_Decrease = Profit_Losses[1]- Profit_Losses[0]   #This calculate the greatest decrease in the profit/losses  over the entire period
    
    for i in range(len(Profit_Losses)):
        
        #The total number of months included in the dataset
        Total += Profit_Losses[i] 

        if i < len(Profit_Losses)-1:
            #The changes in "Profit/Losses" 
            Change = Profit_Losses[i+1]- Profit_Losses[i] 
            #The net total amount of "Profit/Losses" over the entire period
            Total_Change += Change

            #The average of changes in profit & losses
            Avg_Change = round(Total_Change/(len(Profit_Losses)-1),2)
        
            #The greatest increase in profits (date and amount) over the entire period
            if Greatest_Increase < Change:
                Greatest_Increase = Change
                Greatest_Increase_Date= Date[i+1]
            #The greatest decrease in profits (date and amount) over the entire period
            elif Greatest_Decrease > Change:
                Greatest_Decrease = Change
                Greatest_Decrease_Date= Date[i+1]
                
#Result analysis that prints to terminal and export to text file 
print("\nFinancial Analysis")
print("-------------------------")
print("Total Month:", len(Date))
print("Total: $"+ str(Total))
print("Average Change: $"+ str((Avg_Change)))
print("Greatest Increase in Profits:", Greatest_Increase_Date, "($"+ str(Greatest_Increase)+ ")")
print("Greatest Decrease in Profits:", Greatest_Decrease_Date, "($"+ str(Greatest_Decrease)+ ")\n")

f = open("PyBank/Analysis/Results.txt", 'w') 

print("\nFinancial Analysis", file = f)
print("-------------------------", file = f)
print("Total Month:", len(Date), file = f)
print("Total: $"+ str(Total), file = f)
print("Average Change: $"+ str((Avg_Change)), file = f)
print("Greatest Increase in Profits:", Greatest_Increase_Date, "($"+ str(Greatest_Increase)+ ")" , file = f)
print("Greatest Decrease in Profits:", Greatest_Decrease_Date, "($"+ str(Greatest_Decrease)+ ")\n" , file = f)

f.close()