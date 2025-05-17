import heapq
from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        map = Counter(s)
        minHeap = []
        min_del = 0

        for key, val in map.items():
            heapq.heappush(minHeap, (val,key))
            if len(minHeap) > k:
                min_del += minHeap[0][0]
                heapq.heappop(minHeap)

        return min_del