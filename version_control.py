# Version 1

# The purpose of this program is to calculate the house and wage of the user to give them the gross pay per week

# Asks the user for their name
name = input("What is your name?: ")

# Welcomes the user
print("Hi", name.title())
print("")

# Asking the user for hours worked per week
hours = float(input("How many hours do you work per week?: "))
# prints a line break
print("")

# Asking the user for the hourly rate
rate = float(input("What is your hourly rate?: $"))
print("")

# Multiplying the number of hours worked by the hourly rate to get the user's gross pay
weekly_pay = float(hours*rate)

# Printing out the users gross pay
print("You made $", weekly_pay, "this week :)")
