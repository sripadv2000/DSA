class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        maxi, mini = max(nums), min(nums)

        for i in range(mini, maxi):
            if i not in nums:
                res.append(i)
        return res