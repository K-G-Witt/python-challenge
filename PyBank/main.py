# Import required packages:
import os
import csv


# Specify file path for budget_data.csv:
budget_data_path = os.path.join("Resources", "budget_data.csv")


# Generate empty vars and lists to store information needed later:
tot_months = 0
net_prof_loss = 0
previous_prof_loss = 0
change = 0
date = []
prof_loss = []
change_list = []


# Read in budget_data.csv as read-write:
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Defining the header:
    csv_header = next(csvreader)
    
    # Loop through the dataset, starting after the header row:
    for row in csvreader:

        # Define col1 as containing date information:
        date.append(row[0])

        # Define col2 as containing profit/loss information:
        prof_loss.append(row[1])

        # Calculate total number of months:
        tot_months += 1
   
        # Calculate net profit/loss:
        current_prof_loss = int(row[1])
        net_prof_loss += current_prof_loss

        # Calculate month-by-month change in profit/loss:
        if previous_prof_loss != 0:
            monthly_change = current_prof_loss - previous_prof_loss
            # Store these month-by-month changes into a list:
            change_list.append(monthly_change)
        # Update the value of previous profit/loss to the value of the current profit/loss for the next iteration:
        previous_prof_loss = current_prof_loss

    # Calculate average change in profit/loss over the entire period:
    ave_change = sum(change_list)/len(change_list)
    # Round average change in profit/loss to 2 decimal places:
    ave_change = round(ave_change, 2)

    # Calculate the greatest increase in profits:
    increase_prof = max(change_list)

    # Calculate the greatest decrease in profits:
    decrease_prof = min(change_list)

    # Print the analysis to the terminal:
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {tot_months}")
    print(f"Total: ${net_prof_loss}")
    print(f"Average Change: ${ave_change}")
    print(f"Greatest Increase in Profits: (${increase_prof})")
    print(f"Greatest Decrease in Profits: (${decrease_prof})")

    # Export the analysis, as a .txt file, to the Analysis subfolder:
    budget_data_txt = os.path.join("Analysis", "budget_data.txt")
    with open(budget_data_txt, "w") as outfile:
        outfile.write("Financial Analysis\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Months: {tot_months}\n")
        outfile.write(f"Total: ${net_prof_loss}\n")
        outfile.write(f"Average Change: ${ave_change}\n")
        outfile.write(f"Greatest Increase in Profits: (${increase_prof})\n")
        outfile.write(f"Greatest Decrease in Profits: (${decrease_prof})\n")
