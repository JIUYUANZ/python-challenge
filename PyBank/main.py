import os
import csv

budget_data_csv=os.path.join("PyBank","Resources","budget_data.csv")

with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #print(csv_reader)

    csv_header = next(csvfile)
    #print(f"CSV Header:{csv_header}")

    Total_month=0
    Total_amount_Profit=0
    Changes=[]
    front_number=0
    Greatest_increase_change=0
    Greatest_decrease_change=0
    Greatest_increase_month=""
    Greatest_decrease_month=""

    for row in csv_reader:
   
        Total_month +=1

        number=float(row[1])
        Total_amount_Profit=Total_amount_Profit+number 
        
        if front_number != 0:
           change=number - front_number
           Changes.append(change)

           if Greatest_increase_change < change:
              Greatest_increase_change=change
              Greatest_increase_month=row[0]

           elif Greatest_decrease_change > change:
              Greatest_decrease_change=change
              Greatest_decrease_month=row[0]

        front_number=number
        
    print("Total Month:",Total_month)
    print("Total Amount of Profit/Losses:",Total_amount_Profit)
    #print(Changes)

def average(values):
    length=len(values)
    total=0

    for value in values:
        total=total+value

    average=total/length

    return average

print(round(average(Changes),2))

print("Greatest Increase in Profits:",Greatest_increase_month,Greatest_increase_change)
print("Greatest decrease in Profits:",Greatest_decrease_month,Greatest_decrease_change)



  