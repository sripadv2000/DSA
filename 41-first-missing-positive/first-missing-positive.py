class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1 <= ANS <= n+1
        n = len(nums)
        
        # Clean the array
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = (n+1)

        # Mark the presence
        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
        
        # Find the missing positive
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1