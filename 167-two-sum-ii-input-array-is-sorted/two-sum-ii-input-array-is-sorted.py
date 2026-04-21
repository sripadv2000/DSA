class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for idx, val in enumerate(numbers):
            if (target - val) in dict:
                return [dict[target - val], idx + 1]
            dict[val] = idx + 1