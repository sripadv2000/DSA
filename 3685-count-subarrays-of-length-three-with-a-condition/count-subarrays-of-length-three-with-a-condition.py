class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        first, second, third = 0, 1, 2
        N = len(nums)
        res = 0
        while third < N:
            if 2*(nums[first] + nums[third]) == nums[second]:
                res += 1
            first += 1
            second += 1
            third += 1
        return res

        