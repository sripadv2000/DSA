class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        maxi = 0
        for k,v in cnt.items():
            if (k+1) in cnt:
                maxi = max(maxi, v+cnt[k+1])
        return maxi