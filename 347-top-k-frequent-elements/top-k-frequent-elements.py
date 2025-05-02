class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        min_heap = []

        for num in nums:
            hashMap[num] += 1

        for key, val in hashMap.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for key, val in min_heap:
            res.append(val)
        return res