class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for point in points:
            x, y = point
            dist = round(sqrt(x**2 + y**2), 2)
            heapq.heappush(max_heap, (-dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while(max_heap):
            res.append(heapq.heappop(max_heap)[1])
        
        return res