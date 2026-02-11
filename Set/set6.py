n=int(input("Enter number of elements in set: "))
s=set()
for i in range (0,n):
    e=int(input("Enter element: "))
    s.add(e)    
    avg=sum(s)/len(s)
print("Average of set elements is:",avg)