class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1 <= ANS <= n+1
        n = len(nums)
        refer = [0]*(n+1)

        for num in nums:
            if 0 < num < (n+1):
                refer[num] = 1
        
        for i in range(1, n+1):
            if not refer[i]:
                return i
        return n+1
