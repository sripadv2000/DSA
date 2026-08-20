class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 2:
            return nums
        temp1, temp2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if temp1[-1] > temp2[-1]:
                temp1.append(nums[i])
            else:
                temp2.append(nums[i])
        return temp1 + temp2