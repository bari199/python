# Taking user input for two sets and finding their intersection

n=int(input("Enter number of elements in first set: "))
nums = set()

for i in range(n):
    nums.add(int(input("Enter a numbers: ")))

even = {x for x in nums if x%2 == 0}
odd = {x for x in nums if x%2 != 0}

print("Even numbers:", even)
print("Odd numbers:", odd)

