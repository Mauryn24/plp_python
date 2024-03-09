# list of fruits
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

newlist = [x for x in fruits if len(x) % 2 != 0]

print(newlist)

# Prompt user to input words separated by spaces
word_list = input("Enter words separated by spaces: ").split()

# Use list comprehension to filter out words with odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 == 0]

# Display the list of words with odd number of characters
print("Words with odd number of characters:", odd_length_words)

