class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_version = sorted(nums)
        start, end = 0, len(nums)-1
        while start < len(nums) and nums[start] == sorted_version[start]:
            start += 1
        while end > 0 and nums[end] == sorted_version[end]:
            end -= 1
        if end - start >= 0:
            return end - start + 1
        else:
            return 0