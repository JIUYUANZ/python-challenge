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
    print(f"Financial Analysis")
    print(f"----------------------------")    
    print("Total Months:",Total_month)
    print("Total:",Total_amount_Profit)
    #print(Changes)

def average(values):
    length=len(values)
    total=0

    for value in values:
        total=total+value

    average=total/length

    return average

print(f"Average Change: {round(average(Changes),2)}")

print(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_increase_change})")
print(f"Greatest decrease in Profits: {Greatest_decrease_month} (${Greatest_decrease_change})")

analysis_output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(Total_month)}\n"
    f"Total:  ${str(Total_amount_Profit)}\n"
    f"Average Change: ${round(average(Changes),2)}\n"
    f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_increase_change})\n"
    f"Greatest decrease in Profits: {Greatest_decrease_month} (${Greatest_decrease_change})\n"
)

output_path=os.path.join("PyBank","analysis","Analysis_text_file.txt")
with open(output_path,"w",newline="") as txt_file:
    txt_file.write(analysis_output)

  