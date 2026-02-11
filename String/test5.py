# Take input from user
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Split strings into words and convert to sets
words1 = set(s1.split())
words2 = set(s2.split())

# Find common words
common_words = words1 & words2

# Print result
print("The common words are:")
for word in common_words:
    print(word)
