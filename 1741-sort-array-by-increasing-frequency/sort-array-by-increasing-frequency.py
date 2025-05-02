class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = Counter(nums)
        min_heap = []
        
        # Push (frequency, -value) to sort by increasing frequency and decreasing value
        for num in hash_map:
            heapq.heappush(min_heap, (hash_map[num], -num))
        
        res = []
        while min_heap:
            f, val = heapq.heappop(min_heap)
            res.extend([-val] * f)
        return res
        