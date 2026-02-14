class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curRes = sum(nums[:k])
        res = curRes

        iter = k

        while iter<n:
            curRes += nums[iter]
            curRes -= nums[iter-k]
            res = max(curRes, res)
            iter += 1
        return round(res/k,5)