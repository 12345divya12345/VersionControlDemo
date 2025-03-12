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
print("")

print("Your tax can either be 0.17, 0.25, or 0.33")

# Asking the user for their tax rate
tax_rate = float(input("How much is your tax?: "))
print("")

# Calculating the tax deduction by multiplying the tax rate by the weekly pay
tax_deduction = tax_rate*weekly_pay

# Calculating the net income by subtracting the tax deduction from the weekly pay
net_income = weekly_pay - tax_deduction

# Printing out the Net income for the user
print("Your Net Income is $", net_income, ":)")
print("")

# Calculating the yearly income by multiplying the weekly net income by the number of weeks in a year (52)
yearly_income = net_income*52

# Printing out a message which tells the user their yearly income with tax
print("You earn $", yearly_income, "yearly (with tax deduced) :)")

