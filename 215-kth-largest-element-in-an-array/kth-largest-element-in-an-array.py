class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minValue = min(nums)
        maxValue = max(nums)
        countArr = [0] * (maxValue - minValue + 1)
        n = len(countArr)

        for num in nums:
            countArr[num - minValue] += 1
        
        remain = k
        for i in range(n-1, -1, -1):
            remain -= countArr[i]
            if remain <= 0:
                return i + minValue
        return -1