class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        h = []
        for i in range(1,n):
            if heights[i-1] >= heights[i]:
                continue
            
            heapq.heappush(h, heights[i] - heights[i-1])

            while len(h) > ladders:
                x = heapq.heappop(h)
                bricks -= x
            
            if bricks < 0:
                return i - 1
        else:
            return n - 1