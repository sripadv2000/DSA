class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0

        l = 0
        r = 0

        while l<n and r<n:
            if nums[l] != 0:
                l += 1
            elif nums[l] == 0:
                r = l
                while r<n and nums[r] == 0:
                    r += 1
                    res += (r-l)
                l = r

        return res