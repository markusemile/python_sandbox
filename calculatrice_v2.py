number1 = number2 = None

# ask number 1
number1 = input("Enter the first number :")
# check if number is valid
while not number1.isdigit():
    number1 = input("Please, enter a valid number:")

# ask number 2
number2 = input("Enter the second number :")
# check if number is valid
while not number2.isdigit():
    number2 = input("Please, enter a valid number:")

# return the sum of the 2 numbers
print(f"The sum of {number1} and {number2} is equal: {int(number1) + int(number2)}")
