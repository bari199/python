def find_even_odd(a):
    even_set = set()
    odd_set = set()

    for j in a:
        if j%2 == 0:
            even_set.add(j)
        else:
            odd_set.add(j)
    return even_set, odd_set

a = set()
n = int(input("Enter number of elements: "))
for i in range(n):
    b = int(input(f"Enter element {i+1}: "))
    a.add(b)
even_set, odd_set = find_even_odd(a)
print("Even set is:", even_set)
print("Odd set is:", odd_set)
