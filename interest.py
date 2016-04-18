# Prompt the user for an Initial Balance (and save to a variable)
# use the float() function to convert the input into a number.
balance = float(input("Initial balance: "))

# Prompt the user for an Annual Interest % (and save to a variable)
# use the float() function to convert the input into a number
interest = float(input("Annual interest % "))

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!
interest = interest/100

# Prompt the user for a Number of years (and save to a variable)
# use the int() function to convert the input into an integer
years = int(input("Years: "))


def calculate_interest(balance, interest, years):
    new_balance = balance*(1+(interest/12))**(12*years)
    interest_earned = new_balance - balance
    return interest_earned

# Output the interest earned 
# interest_earned is now a local variable! need to define function
earned = calculate_interest(balance,interest,years)
output = "Interest earned in "+str(years)+" years: $"+str(earned)
# output = "Interest earned in "+str(years)+" years: $"+str(interest_earned)
print(output)

# Output the total value
print("Total value after "+str(years)+" years: $"+str(earned + balance))
# print("Total value after "+str(years)+" years: $"+str(new_balance))
# Traceback (most recent call last):
#   File "interest.py", line 31, in <module>
#     print("Total value after "+str(years)+" years: $"+str(new_balance))
# NameError: name 'new_balance' is not defined

