class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, val in enumerate(nums):
            if val in mapping:
                return [mapping[val], idx]
            mapping[target - val] = idx
        return [-1, -1]
