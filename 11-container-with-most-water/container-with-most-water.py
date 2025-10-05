class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxArea = 0
        # n = len(height)

        # for l in range(n):
        #     for r in range(l+1, n):
        #         area = (r-l) * min(height[l], height[r])
        #         maxArea = max(area, maxArea)
        # return maxArea

        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        