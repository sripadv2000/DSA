class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            dist = abs(num - x)
            heapq.heappush(max_heap, (-dist, -num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = [-heapq.heappop(max_heap)[1] for _ in range(k)]
        res.sort()
        return res