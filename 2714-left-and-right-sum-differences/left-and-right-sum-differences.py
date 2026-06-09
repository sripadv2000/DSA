class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = [0]*n, [0]*n
        res = [0]*n

        for i in range(1, n):
            pre[i] = nums[i-1] + pre[i-1]
        
        for i in range(n-2, -1, -1):
            suf[i] = nums[i+1] + suf[i+1]
        
        for i in range(n):
            res[i] = abs(pre[i] - suf[i])
        
        return res

