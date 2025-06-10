class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        res = cnt.values()

        odd_max = max(x for x in res if x % 2 == 1)
        even_min = min(x for x in res if x % 2 == 0)

        return odd_max - even_min