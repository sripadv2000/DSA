class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashset = set(nums)
        ans = k
        while ans in hashset:
            ans += k
        return ans