class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -1 * num)

        # make sure every num in left <=. every num in right
        if (self.left and self.right and 
            ((-1 * self.left[0]) > self.right[0])):
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        #unequal size
        if len(self.left) > len(self.right) + 1:
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-1 * self.left[0] + self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()