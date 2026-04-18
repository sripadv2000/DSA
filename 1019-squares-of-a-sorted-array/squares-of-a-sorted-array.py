class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l, r, iter = 0, length-1, length-1
        res = [0]*length

        while iter >= 0:
            if nums[l]**2 < nums[r]**2:
                res[iter] = nums[r]**2
                iter -= 1
                r -= 1
            else:
                res[iter] = nums[l]**2
                iter -= 1
                l += 1
        return res
