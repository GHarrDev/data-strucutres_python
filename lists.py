print("-----------------------------------------------------------------")
monthly_expenses = [{"month": "January", "expenses": 2200},
                    {"month": "February", "expenses": 2350},
                    {"month": "March", "expenses": 2600},
                    {"month": "April", "expenses": 2130},
                    {"month": "May", "expenses": 2190}
                   ]

# Question 1:
# In Feb, how many more dollars were spent compared to January?
jan = 0
feb = 0

for entry in monthly_expenses:
    if entry["month"] == "January":
        jan = entry["expenses"]
    elif entry["month"] == "February":
        feb = entry["expenses"]

res1 = feb - jan

print(f"1. The difference in expenses from January to February is ${res1}.\n")

# Question 2:
# Find out the total expense for the first quarter.
mar = 0

for entry in monthly_expenses:
    if entry["month"] == "January":
        jan = entry["expenses"]
    elif entry["month"] == "February":
        feb = entry["expenses"]
    elif entry["month"] == "March":
        mar = entry["expenses"]

res2 = jan + feb + mar

print(f"2. The total expense for the first quarter is ${res2}.\n")

# Question 3:
# Find out if you spent exactly $2000 in any month.
res3 = None

for entry in monthly_expenses:
    if entry["expenses"] == 2000:
        res3 = entry["month"]
if res3:    
    print(f"3. Exactly $2000 was spent in the month of {res3}.\n")
else:
    print(f"3. Exactly $2000 was spent in no month.\n")



# Question 4:
# June just finished and your expenses were $1980. Add this to the monthly expense list.
monthly_expenses.append({"month": "June", "expenses": 1980})

print("4. Updated list:")
for entry in monthly_expenses:    
    print(f"{entry["month"]} - {entry["expenses"]}")


# Question 5:
# You've returned an item purchased in April and received a $200 refund. Update the monthly expense list.
refund = 200

for entry in monthly_expenses:
    if entry["month"] == "April":
        entry["expenses"] -= refund

print("\n5. Update list:")
for entry in monthly_expenses:
    print(f"{entry["month"]} - {entry["expenses"]}")