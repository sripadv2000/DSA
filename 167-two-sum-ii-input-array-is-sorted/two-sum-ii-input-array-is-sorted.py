class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left<right:
            curr_sum = (numbers[left]+numbers[right])
            if curr_sum == target:
                break
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return [left+1,right+1]