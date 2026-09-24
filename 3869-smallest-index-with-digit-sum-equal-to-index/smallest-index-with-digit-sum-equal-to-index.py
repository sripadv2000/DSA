class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            summ = 0
            while num:
                summ += num % 10
                num //= 10
            return summ
        
        for i in range(len(nums)):
            if i == sumOfDigits(nums[i]):
                return i
        return -1