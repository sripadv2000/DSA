class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 37
        for num in nums:
            digit = 0
            while num > 0:
                digit += num % 10
                num //= 10
            res = min(res, digit)
        return res
