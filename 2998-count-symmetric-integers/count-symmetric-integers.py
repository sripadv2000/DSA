class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        iter = low
        for iter in range(low, high + 1):
            s = str(iter)
            N = len(s)
            
            if N%2 == 1:
                continue
            
            half = N // 2
            left = sum(int(s[i]) for i in range(half))
            right = sum(int(s[i]) for i in range(half, N))
            
            if left == right:
                res += 1
        return res