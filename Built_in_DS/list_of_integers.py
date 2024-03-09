# Instantiate an empty list to store integers
numbers = []

# Prompt user to input integers
for i in range(5):
    number = int(input("Enter an integer: "))  # Prompt user for input and convert it to an integer
    numbers.append(number)  # Add the integer to the list

# Calculate the sum of integers in the list
sum = 0
for number in numbers:
    sum += number

# Display the sum
print("The sum is", sum)
