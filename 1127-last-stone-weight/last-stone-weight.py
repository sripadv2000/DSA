import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for num in stones:
            heapq.heappush(maxheap, -num)
        
        while len(maxheap) > 1:
            first = -heapq.heappop(maxheap)
            second = -heapq.heappop(maxheap)
            if first != second:
                heapq.heappush(maxheap, -(first-second))

        return 0 if len(maxheap) == 0 else -maxheap[0]