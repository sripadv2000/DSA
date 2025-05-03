class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        max_heap = []

        for i in range(rows):
            for j in range(cols):
                heapq.heappush(max_heap, -matrix[i][j])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        return -max_heap[0]