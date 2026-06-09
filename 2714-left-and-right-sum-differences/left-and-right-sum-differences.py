class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        left_sum = 0
        for i in range(n):
            res[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        
        for i in range(n-1, -1, -1):
            res[i] = abs(res[i] - right_sum)
            right_sum += nums[i]
        
        return res

