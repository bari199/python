def second_largest_from_set():
    a = set()
    n = int(input("Enter number of elements: "))

    for i in range(n):
        b = int(input(f"Enter element {i+1}: "))
        a.add(b)

    if len(a) < 2:
        print("Second largest element not possible")
        return

    sorted_set = sorted(a)

    print("Sorted set is:", sorted_set)
    print("Second largest element is:", sorted_set[-2])

second_largest_from_set()
