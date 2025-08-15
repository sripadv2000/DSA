import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n=4^x
        # logn_4 = x
        if(n==1):
            return True
        if(n<=0):
            return False
        ln = math.log(n,4)
        if(ln == int(ln)):
            return True
        else:
            return False
