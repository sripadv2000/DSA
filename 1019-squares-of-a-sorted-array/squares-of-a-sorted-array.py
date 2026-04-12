class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, iter = 0, n-1, n-1
        res = [0]*n

        while (iter >= 0):
            if nums[l]**2 > nums[r]**2:
                res[iter] = nums[l]**2
                l += 1
            else:
                res[iter] = nums[r]**2
                r-=1
            iter -= 1

        return res
