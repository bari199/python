def average_of_set(n):
    s = set()
    
    for i in range(n):
        e = int(input(f"Enter element:{i+n} "))
        s.add(e)
    
    avg = sum(s) / len(s)
    return avg


# Main program
n = int(input("Enter number of elements in set: "))
result = average_of_set(n)
print("Average of set elements is:", result)
