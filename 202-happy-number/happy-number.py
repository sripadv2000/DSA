class Solution:
    def isHappy(self, n: int) -> bool:
        usedIntegers = set()
        while 1:
            summ = 0
            while n!=0:
                summ += (n%10)**2
                n //= 10
            if summ == 1:
                return True
            n = summ
            if n in usedIntegers:
                return False
            usedIntegers.add(n)
