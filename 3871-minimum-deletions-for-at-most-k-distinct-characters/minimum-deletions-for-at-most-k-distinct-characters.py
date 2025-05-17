import heapq
from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        map = Counter(s)
        minHeap = []
        min_del = 0

        for val in map.values():
            heapq.heappush(minHeap, val)
            if len(minHeap) > k:
                min_del += heapq.heappop(minHeap)

        return min_del