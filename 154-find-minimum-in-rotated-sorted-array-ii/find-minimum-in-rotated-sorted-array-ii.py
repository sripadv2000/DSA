class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 5001
        for num in nums:
            if num < minimum:
                minimum = num
        return minimum