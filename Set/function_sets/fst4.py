#Function that returns even and odd sets
def find_even_odd(num):
    even_set = set()
    odd_set = set()

    for n in num:
        if n%2 == 0:
            even_set.add(n)
        else:
            odd_set.add(n)
    return even_set, odd_set

num = int(input("Enter number of elements in the set: "))

even, odd = find_even_odd(num)
print("Even numbers:", even)
print("Odd numbers:", odd)

