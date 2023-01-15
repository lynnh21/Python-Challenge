import os
import csv
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
# List to store data
date = []
profit_or_loss = []
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read header row
    csv_header = next(csvreader)

    total_months = 0
    total_amount = 0
    amount_list = []
    date_list = []
    for row in csvreader:
        # Total number of months
        total_months = total_months + 1
        # Total amount
        total_amount = total_amount + int(row[1])

        # Changes
        amount_list.append(int(row[1]))
        date_list.append(row[0])
    change_list = []

    def average(a):
        return sum(a)/len(a)
    for x in range(1, 86):
        change = amount_list[x] - amount_list[x-1]
        change_list.append(change)
        # Greatest increase profit
    greatest_increase = 0
    greatest_increase_index = 0
    for x in range(len(change_list)):
        if change_list[x] > greatest_increase:
            greatest_increase = change_list[x]
            greatest_increase_index = x
        else:
            greatest_increase = greatest_increase
            greatest_increase_index = greatest_increase_index
        # Greatest decrease
    greatest_decrease = 0
    greatest_decrease_index = 0
    for x in range(len(change_list)):
        if change_list[x] < greatest_decrease:
            greatest_decrease = change_list[x]
            greatest_decrease_index = x
        else:
            greatest_decrease = greatest_decrease
            greatest_decrease_index = greatest_decrease_index
    print(f"Total Month : {total_months}")
    print(f"Total : ${total_amount}")
    print(f"Average change = ${round(average(change_list),2)}")
    print(
        f"Greatest Increase in Profits: {date_list[greatest_increase_index + 1]} (${greatest_increase})")
    print(
        f"Greatest Decrease in Profits: {date_list[greatest_decrease_index + 1]} (${greatest_decrease})")
# Export to text
output_path = os.path.join("Analysis", "pybank_result.txt")

with open(output_path, 'w') as txt:
    txt.write("Financial Analysis \n")
    txt.write(f"-------------------------- \n")
    txt.write(f"Total Month : {total_months} \n")
    txt.write(f"Total Month : {total_amount} \n")
    txt.write(f"Average change = ${round(average(change_list),2)}\n")
    txt.write(
        f"Greatest Increase in Profits: {date_list[greatest_increase_index + 1]} (${greatest_increase})\n")
    txt.write(
        f"Greatest Decrease in Profits: {date_list[greatest_decrease_index + 1]} (${greatest_decrease})\n")
