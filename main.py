#total number of months in dataset
#net total amount of Profit/Losses over the entire period
#average of the changes in Profit/Losses over the entire period
#greatest increase in profit  (data & amount) over the entire period
#greatest decrease in losses (data & amount) over the entire period


#import os module to create file paths across operating systems
import os

#module for reading CSV files
import csv

#load files
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#variables
total_months = 0
net_total_amount = 0
average_change = 0
profit_money = 0
loss_money = 0
initial_profit = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
net_profit_loss = 0

#lists 
months = []
date = []
profit_loss = []


#open & create a new header row
with open(budget_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row first
    csv_reader = next(csv_file)

    #print(f"CSV Header: {csv_header}")


#looping
for row in csv_reader:

    #total number of months in dataset 
    #total_months
    total_months +=1

    #calculate monthly change 
    #calcuate the change
    current_month_profit_loss = int(row[1])
    net_profit_loss += current_month_profit_loss

    #storing
    #set to 1
    if (total_months ==1):
        #net total amount of Profit/Losses over the entire period
        #net_total_amount
        previous_month_profit_loss = current_month_profit_loss

    else:
        #this is the part where I skipped
        #change in profit loss
        profit_loss_change = current_month_profit_loss - previous_month_profit_loss

        #month changes append
        date.append(row[0])

        #profit loss append
        profit_loss_change.append(profit_loss_change)

        #loop for next
        previous_month_profit_loss = current_month_profit_loss

    #average of the changes in Profit/Losses over the entire period
    #average_change
    average_change = round(net_total_amount/months, 2)


    #greatest increase in profit  (date & amount) over the entire period
    #max_months & max_money
    max_money = max(month_change)
    max_month = date[month_changes.index(max_money)]

    #greatest decrease in losses (date & amount) over the entire period
    #min_month & min_money
    min_money = min(month_change)
    min_month = date[(month_change.index(min_money))]

    #name it
    max_month = months[max_money]
    min_month = months[min_money]


#print analysis
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total_amount}")
# add $ for money
print(f"Average Change: {average_change}")
#add $ for money
print(f"Greatest Increase in Profits: {max_month} (${max_money})")
#add $ for money
print(f"Greatest Decrease in Profits: {min_month} (${min_money})")
