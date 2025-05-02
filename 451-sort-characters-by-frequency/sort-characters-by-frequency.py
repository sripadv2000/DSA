class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = Counter(s)
        max_heap = []
        
        for num in hash_map:
            heapq.heappush(max_heap, (-hash_map[num], num))
            
        res = ""
        while max_heap:
            f, val = heapq.heappop(max_heap)
            res += val * -f
        
        return res