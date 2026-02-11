# even and odd number sets using functions 
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

even_set = set()
odd_set = set()

for n in nums:
    if n%2 == 0:
        even_set.add(n)
    else:
        odd_set.add(n)

print("Even numbers:", even_set)
print("Odd numbers:", odd_set)

