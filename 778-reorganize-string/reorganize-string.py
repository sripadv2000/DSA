import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        N = len(s)
        minHeap = []

        for char in s:
            heapq.heappush(minHeap, (-count[char], char))

        res = [0]*N
        idx = 0
        while idx < N:
            res[idx] = heapq.heappop(minHeap)[1]
            idx += 2
            
        idx = 1
        while idx < N:
            res[idx] = heapq.heappop(minHeap)[1]
            idx += 2
        if N == 1:
            return s
        if res[0] == res[1]:
            return ""
        return "".join(res)