s={1,2,3,4,5}



#add method to add elements to set
s.add(6)
s.add("hello")
#s.add(True)
s.add(3.14)

#update method to add multiple elements to set
s.update([7,8,9])

s.remove(6)
s.discard(9)
s.pop()
#s.clear()

s2= s.copy()
print(s)
print(s2)