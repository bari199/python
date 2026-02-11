string=input('Enter a String: ')

count1=0
count2=0
count3=0
count4=0

for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
    elif(i.isdigit()):
        count3=count3+1
    else:
        count4=count4+1
        
print("The lower string is:",count1)
print("The upper string is:",count2)
print("The Total digit is: ",count3)
print("The Total number is special charecter is:",count4)
