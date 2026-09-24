class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            temp = num
            summ = 0
            while temp:
                summ += temp % 10
                temp //= 10
            return summ
        
        for i in range(len(nums)):
            if i == sumOfDigits(nums[i]):
                return i
        return -1