# Prompt user for first set of integers
set1 = set()
for i in range(5):
    number = int(input("Enter an integer: "))  # Prompt user for input and convert it to an integer
    set1.add(number)  # Add the integer to the set

# display the set
print(f"First set of integers:{set1}")

# Prompt user for second set of integers
set2 = set()
for i in range(5):
    number = int(input("Enter an integer: "))  # Prompt user for input and convert it to an integer
    set2.add(number)  # Add the integer to the set

# display the set
print(f"Second set of integers:{set2}")

# display common integers
print("Common integers:")
print(set1.intersection(set2))