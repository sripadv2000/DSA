class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        cnt = Counter(nums)

        for key,val in cnt.items():
            heapq.heappush(min_heap, [val,key])
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [val for key, val in min_heap]