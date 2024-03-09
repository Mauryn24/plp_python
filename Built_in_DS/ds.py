# Create an empty list called my_list
my_list = []

# Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Print the updated list
print(my_list)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Print the updated list
print(my_list)

# Remove the last element from my_list
my_list.pop()

# Print the updated list
print(my_list)

# Sort my_list in ascending order
my_list.sort()

# Print the updated list
print(my_list)

# Find the index of a number in my_list
number_to_find = 30
index = my_list.index(number_to_find)

# Print the index of the number
print(f"The number {number_to_find} is at index {index}")
