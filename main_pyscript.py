import csv
from pathlib import Path
csv_path = Path("budget_data.csv")

with open(csv_path, "r") as file:
    csv_file = csv.reader(file, delimiter = ",")
    
    headers = next(csv_file)
    #yield the first one so on the next for loop, it takes it out
    
    whole_list = []
    for x in csv_file:
        whole_list.append(x)
    #transferring all data to a list from the csv file
    
t_months = len(whole_list)
#total months is lenght of whole list minus header

money_list = [row[1] for row in whole_list]
#list for just second row of money

t_money = 0
for ele in range(0, len(money_list)):
    
    t_money = t_money + int(money_list[ele])
#this for loop adds all values in that list of money

change_list = []
for ele in range(0, len(money_list)):
    current_change = int(money_list[ele]) - int(money_list[ele - 1])
    change_list.append(current_change)
#list is created with only the changes month to month

change_list.pop(0)
#first item of list is erased given that a change month to month cannot have the first month as a corresponding month.

avg_change = 0
t_change = 0
for ele in range(0, len(change_list)):
    t_change = t_change + int(change_list[ele])
    
avg_change = t_change/len(change_list)
print(avg_change)
#calculating the average change of profits/losses

changelist_int = []
int_value = 0
for ele in range(0, len(change_list)):
    int_value = (int(change_list[ele]))
    changelist_int.append(int_value)
print(changelist_int)
#changing previous list into all integers

greatest_profit = max(changelist_int)
lowest_profit = min(changelist_int)

index_greatest = 0
index_lowest = 0
for ele in range(0, len(changelist_int)):
    if changelist_int[ele] == greatest_profit:
        index_greatest = ele
    if changelist_int[ele] == lowest_profit:
        index_lowest = ele
#getting the index position of greatest and lowest

greatest_month = whole_list[index_greatest + 1][0]
lowest_month = whole_list[index_lowest + 1][0]
#using previous index position to correspond with month but adding 1 because previously we had taken out 1

with open("output.txt", "w") as f:
    print('Financial Analysis', file=f)
    print('--------------------------------------------', file=f)
    print('Total Months: ' + str(t_months), file=f)
    print('Total: $' + str(t_money), file =f)
    print('Greatest Increase in Profits: ' + greatest_month + ' ' + str(greatest_profit), file=f)
    print('Greatest Decrease in Profits: ' + lowest_month +' ' + str(lowest_profit), file=f)
#printing to an output file