class Number:
    def __init__(self, n):
        self.n=n
class EvenOdd(Number):
    def check(self):
        if self.n%2==0:
            print(self.n,"is even number")
        else:
            print(self.n,"is odd number")

class Prime(Number):
    def check(self):
        if self.n > 1:
           for i in range(2, self.n):
               if (self.n % i) == 0:
                   print(self.n,"is not a prime number")
                   break
               else:
                   print(self.n,"is a prime number")
                   break
        else:
           print(self.n,"is not a prime number")  

class Perfect(Number):
    def check(self):
        sum=0
        for i in range(1,self.n):
            if self.n%i==0:
                sum+=i
                if sum==self.n:
                    print(self.n,"is a perfect number")
                else:
                    print(self.n,"is not a perfect number")
         
            

e=EvenOdd(10)
f=Prime(10)
g=Perfect(6)
e.check()
f.check()
g.check()

