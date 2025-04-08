class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) != len(set(nums)):
            ops += 1
            nums = nums[3:]
        return ops