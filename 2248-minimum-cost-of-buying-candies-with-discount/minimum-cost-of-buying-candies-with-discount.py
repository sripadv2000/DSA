class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = sum(cost)

        cost.sort(reverse = True)
        free = 2

        while free < len(cost):
            res -= cost[free]
            free += 3
        return res