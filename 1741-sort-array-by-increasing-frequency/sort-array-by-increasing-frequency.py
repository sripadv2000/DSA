class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = Counter(nums)
        max_heap = []
        
        # Push (frequency, -value) to sort by increasing frequency and decreasing value
        for num in hash_map:
            heapq.heappush(max_heap, (hash_map[num], -num))
        
        res = []
        while max_heap:
            f, neg_val = heapq.heappop(max_heap)
            res.extend([-neg_val] * f)
        return res
        