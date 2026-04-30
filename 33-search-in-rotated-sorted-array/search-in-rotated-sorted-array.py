from collections import Counter
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 153. Find Minimum in Rotated Sorted Array
        def findPivot(nums):
            if len(nums) == 1:
                return 0
            left, right = 0, len(nums) - 1

            if nums[right] > nums[left]:
                return left

            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid - 1] > nums[mid]:
                    return mid
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] > nums[0]:
                    left = mid + 1
                if nums[mid] < nums[0]:
                    right = mid - 1
        
        def binarySearch(l, r):
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        n = len(nums)
        pivot = findPivot(nums)

        # If array is not rotated, search full array
        if pivot == 0:
            return binarySearch(0, n - 1)

        # Decide which sorted half to search
        if nums[0] <= target <= nums[pivot - 1]:
            return binarySearch(0, pivot - 1)
        else:
            return binarySearch(pivot, n - 1)