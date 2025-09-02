class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        N = len(points)

        for i in range(N):
            x1, y1 = points[i][0], points[i][1]
            for j in range(N):
                x2, y2 = points[j][0], points[j][1]
                if i == j or not (x1 <= x2 and y1 >= y2):
                    continue
                if N == 2:
                    ans += 1
                    continue
                illegal = False
                for k in range(N):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k][0], points[k][1]
                    isXContained = (x3 >= x1 and x3 <= x2)
                    isYContained = (y3 <= y1 and y3 >= y2)
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans
