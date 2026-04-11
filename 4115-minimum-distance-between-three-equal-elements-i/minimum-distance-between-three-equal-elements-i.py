class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 2*n
        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j+1, n):
                    if nums[j]==nums[k]:
                        res = min(2*(k-i), res)
                        break

        if res != 2*n:
            return res
        else:
            return -1