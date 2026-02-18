class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n))
        return not('11' in s or '00' in s)