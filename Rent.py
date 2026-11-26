#inputs we need to get from the user
# total rent amount
# total food cost 
# personal expenses
# output
# total amount of money spent


rent = int(input("Enter the total rent amount: "))
food = int(input("Enter the total food cost: "))
expenses = int(input("Enter the personal expenses: "))
khala = int(input("Enter the amount spent on khala: "))
wifi = int(input("Enter the amount spent on wifi: "))


total = rent + food + expenses + khala + wifi
print("The total amount of money spent is:", total)