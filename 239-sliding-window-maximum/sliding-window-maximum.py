from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # use deque
        # keep adding elements to deque if number is smaller
        # if you get any greater element, then keep popping
        # if element removed from array is the left most in deque, pop from deque too.
        res = []
        q = deque()
        l, r = 0, 0
        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
        