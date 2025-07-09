class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []

        def countOnes(num):
            res = 0
            while num:
                res += num & 1
                num >>= 1
            return res
        
        for i in range(0, n+1):
            arr.append(countOnes(i))

        return arr