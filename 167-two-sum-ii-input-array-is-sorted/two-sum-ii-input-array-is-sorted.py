class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 1, n
        while left<right:
            curr_sum = (numbers[left-1]+numbers[right-1])
            if curr_sum == target:
                break
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return [left,right]