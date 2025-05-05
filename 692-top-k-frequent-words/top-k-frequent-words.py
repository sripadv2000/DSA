class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = Counter(words)
        min_heap = []

        for key, val in hash_map.items():
            heapq.heappush(min_heap, (-val, key))

        res = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return res