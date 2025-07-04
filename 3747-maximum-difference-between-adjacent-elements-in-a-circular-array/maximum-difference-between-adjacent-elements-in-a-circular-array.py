class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        length = len(nums)
        max_diff = abs(nums[0] - nums[length-1])
        for i in range(1, length):
            max_diff = max(max_diff, abs(nums[i] - nums[i-1]))
        return max_diff