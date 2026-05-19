class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minheap1, minheap2 = [], []
        
        p1 = 0
        while p1 < len(nums1):
            heapq.heappush(minheap1, nums1[p1])
            p1 += 1
        p2 = 0
        while p2 < len(nums2):
            heapq.heappush(minheap2, nums2[p2])
            p2 += 1
        
        while minheap1 and minheap2:
            if minheap1[0] == minheap2[0]:
                return minheap1[0]
            elif minheap1[0] < minheap2[0]:
                heapq.heappop(minheap1)
            else:
                heapq.heappop(minheap2)
        
        return -1