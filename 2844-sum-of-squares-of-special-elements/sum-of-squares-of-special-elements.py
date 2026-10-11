class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        N = len(nums)
        squares = 0
        for i in range(N):
            if N % (i+1) == 0:
                squares += nums[i]**2
        return squares
