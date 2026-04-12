class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num**2)
        res = []
        while minheap:
            res.append(heapq.heappop(minheap))
        return res
