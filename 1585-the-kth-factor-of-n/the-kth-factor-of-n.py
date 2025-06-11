class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = [-1]
        for i in range(1, n+1):
            if n%i == 0:
                res.append(i)

        kth = 0
        if len(res) > k:
            return res[k]
        else:
            return -1