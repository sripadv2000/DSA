class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        s = set()
        cnt = 0

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j] and j not in s:
                    s.add(j)
                    cnt += 1
                    break

        return (n-cnt)