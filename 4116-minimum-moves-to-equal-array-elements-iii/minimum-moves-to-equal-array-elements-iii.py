class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        res = 0
        for num in nums:
            res += maximum - num
        return res