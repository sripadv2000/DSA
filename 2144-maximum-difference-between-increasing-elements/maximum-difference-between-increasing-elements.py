class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        min_element = nums[0]
        max_diff = -1
        for i in range(1, length):
            if (nums[i] > min_element) and (nums[i] - min_element) > max_diff:
                max_diff = nums[i] - min_element
            if nums[i] < min_element:
                min_element = nums[i]
        return max_diff