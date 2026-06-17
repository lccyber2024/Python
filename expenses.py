#expenses = [10.50, 8.5, 15, 20, 5, 3 ]
#sum = 0 
#for x in expenses:
#    sum = sum + x
#print("You spent: $" + str(sum))

total = 0 
expenses = []

for i in range(7):
    expenses.append(float(input("Enter expense " + str(i + 1) + ": ")))

    total = sum(expenses)
print("You spent: $" + str(total))
