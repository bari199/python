class SmartNumber(list):
    def even(self):
        return [n for n in self if n%2 == 0]
    def odd(self):
        return [n for n in self if n%2 != 0]
    def is_prime(self,n):
        if n<=1:
            return False
        for i in range (2, n):
            if n%i == 0:
                return False
        return True
    def prime(self):
        return [n for n in self if self.is_prime(n)]
    def is_perfect(self,n):
        if n<=1:
            return False
        return sum(i for i in range(1, n) if n%i == 0) == n
    
    def perfect(self):
        return [n for n in self if self.is_perfect(n)]
    
num = SmartNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Even numbers:", num.even())
print("Odd numbers:", num.odd())
print("Prime numbers:", num.prime())
print("Perfect numbers:", num.perfect())


        
