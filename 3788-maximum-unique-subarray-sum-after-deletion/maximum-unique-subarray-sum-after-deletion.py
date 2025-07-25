class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        maxi = -101
        res = 0
        for num in nums:
            maxi = max(maxi, num)
        if maxi < 0:
            return maxi
        s = set()
        for num in nums:
            if num not in s and num > 0:
                s.add(num)
                ans += num
                res = max(ans, res)
        return res