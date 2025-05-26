class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        low, high = 0, N-1

        # 1. Find the first index violating ascending order
        while low < N-1 and nums[low] <= nums[low + 1]:
            low += 1
        
        # 2. Find the first index violating descending order
        while high > 0 and nums[high - 1] <= nums[high]:
            high -= 1
        
        # If low >= high means that the array is already sorted.
        if low >= high:
            return 0
        
        # 3. Find min and max of our temporary window nums[lo: hi + 1]
        windowMax = max(nums[low:high+1])
        windowMin = min(nums[low:high+1])

        # 4. Extend the window to left side if it violates windowMin
        while low > 0 and nums[low - 1] > windowMin:
            low -= 1
        
        # 5. Extend the window to right side if it violates windowMax
        while high < N-1 and nums[high + 1] < windowMax:
            high += 1
        
        return high - low + 1