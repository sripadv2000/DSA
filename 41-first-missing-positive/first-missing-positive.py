class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        elements = set()
        for i in range(n):
            if nums[i] > 0:
                elements.add(nums[i])

        for i in range(1,n+2):
            if i not in elements:
                return i