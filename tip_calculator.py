print("Welcome to Donells tip calculator project!")


print ("A Meal For One") 
# The total cost of this meal was $15.
# Only one person is paying.
# It's a 20% tip.
# The should come out to $19.50

# The variable "bill" asks for the bill from the user
# Ask the user for a input how much did the food cost and what was the total bill. 
food = float(input("How much did the food cost? $")) 
bill = float(input("What was the total bill? $"))
tip = int(input("How much is the tip?"))
people = int(input("How many is splitting the bill?"))
bill_with_tip = bill / 100

# "user input" for the variable {bill_with_tip} divided by 100 is the percentage equation and is assigned to a variable.

print(f"This person should pay ${bill_with_tip}")

# Calculates the bill


print("A Feast to Remember")
#If the food was 250,000.00, split between 3 people, with a 31% tip!
# The total cost of the bill $35,250,000.00
# Each person should pay $11,750,000.00 


food = float(input("How much did the food cost?"))
bill = float(input("What was the total bill? $"))
tip = int(input("How much is the tip?"))
people = int(input("How many people is splitting the bill?"))
bill_with_tip = tip / 100 * bill + food 
print(f"Each person should pay ${bill_with_tip}.")

print("No Tip")
# The meal is $78.99.
# The total cost of the meal is $86.89
# The bill is getting split between 6 people.
# There's no tip.
# The outcome should be $14.98. 

food = float(input("How much did the food cost?"))
bill = float(input("What was the total bill? $"))
tip = int(input("How much is the tip?"))
people = int(input("How many people is splitting the bill?"))
bill_no_tip = bill / people
print(f"Each person should pay ${bill_no_tip}.")

print("Sharing the bill among many")
# The meal is 5000.
# The total bill is $6,100.00.
# 879 people are paying.
# There's at 12% tip. 
# Everyone should pay 6.96 each.

food = float(input("How much did the food cost?"))
bill = float(input("What was the total bill? $"))
tip = int(input("How much is the tip?"))
people = int(input("How many people is splitting the bill?"))
bill_with_tip = bill / people
print(f"Each person should pay ${bill_with_tip}.")