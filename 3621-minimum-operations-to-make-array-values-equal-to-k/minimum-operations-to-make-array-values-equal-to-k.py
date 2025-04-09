class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        s = set(nums)
        greater = 0
        for num in s:
            if num > k:
                greater += 1
        return greater