class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        res = []
        
        for i in range(len(nums)):
            heapq.heappush(maxheap, (-nums[i], i))
            
            # Lazy deletion: pop stale elements
            while maxheap[0][1] < i - k + 1:
                heapq.heappop(maxheap)
            
            if i >= k - 1:
                res.append(-maxheap[0][0])
        
        return res