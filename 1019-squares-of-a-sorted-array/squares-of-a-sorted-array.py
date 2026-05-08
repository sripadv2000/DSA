class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length

        left, right, iter = 0, length - 1, length - 1

        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2

            if left_square > right_square:
                res[iter] = left_square
                left += 1
            else:
                res[iter] = right_square 
                right -= 1

            iter -= 1
        return res


