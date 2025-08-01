class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(0, len(nums), 3):
            if (nums[i+2] - nums[i]) > k:
                return []
            else:
                output.append([nums[i],nums[i+1],nums[i+2]])
        return output