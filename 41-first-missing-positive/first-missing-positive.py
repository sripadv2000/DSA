class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1 <= ANS <= n+1
        n = len(nums)
        refer = [0]*(n+2)

        for num in nums:
            if num > 0 and num < (n+1):
                refer[num] += 1
        
        for i in range(1, n+2):
            if refer[i] == 0:
                return i
