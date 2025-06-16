class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        max_diff = -1
        for i in range(0, length - 1):
            for j in range(i+1, length):
                if nums[j] > nums[i]:
                    max_diff = max(max_diff, nums[j] - nums[i])
        return max_diff
