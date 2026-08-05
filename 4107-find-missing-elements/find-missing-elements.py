class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        res = []
        maxi, mini = max(nums), min(nums)

        for i in range(mini, maxi):
            if i not in seen:
                res.append(i)
        return res