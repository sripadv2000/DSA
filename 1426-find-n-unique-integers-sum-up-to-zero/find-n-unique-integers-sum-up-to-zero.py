class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n%2 == 1:
            res.append(0)
            n -= 1
        i = 1
        while n > 0:
            res.append(i)
            res.append(-i)
            i += 1
            n -= 2
        return res