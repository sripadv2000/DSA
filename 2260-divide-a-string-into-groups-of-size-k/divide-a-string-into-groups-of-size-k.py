class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        N = len(s)
        remainder = N % k

        for i in range(0,N,k):
            res.append(s[i:i+k])
            
        if remainder != 0:
            res[-1] = res[-1] + fill * (k - N % k)

        return res