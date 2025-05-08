class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            current_element = nums[i]
            stored_element = target-nums[i]
            if stored_element in dict:
                return [dict[stored_element], i]
            dict[current_element] = i