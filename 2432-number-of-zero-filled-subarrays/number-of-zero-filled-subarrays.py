class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        d = defaultdict(int)

        l = 0
        r = 0

        while l<n and r<n:
            if nums[l] != 0:
                l += 1
            elif nums[l] == 0:
                r = l
                while r<n and nums[r] == 0:
                    r += 1
                d[r-l] += 1
                l = r

        res = 0
        for k, v in d.items():
            res += (k*(k+1)//2)*v
            
        return res