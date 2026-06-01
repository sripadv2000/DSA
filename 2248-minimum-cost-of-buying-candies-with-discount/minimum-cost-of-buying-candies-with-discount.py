class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        res = sum(cost)

        if n < 3:
            return res

        cost.sort(reverse = True)
        free = 2

        while free < n:
            res -= cost[free]
            free += 3
        return res

