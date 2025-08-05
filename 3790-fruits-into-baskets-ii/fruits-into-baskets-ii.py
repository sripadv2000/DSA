class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        cnt = 0

        for i in range(n):
            for j in range(n):
                if not used[j] and fruits[i] <= baskets[j]:
                    used[j] = True
                    cnt += 1
                    break

        return (n - cnt)