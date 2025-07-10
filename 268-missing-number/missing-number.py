class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        N = len(nums)
        for i in range(N):
            xor ^= nums[i]
            xor ^= i+1
        return xor