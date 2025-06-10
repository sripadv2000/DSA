class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        res = sorted(cnt.values())
        odd_max, even_min = 0,0
        for num in res:
            if num % 2 == 0:
                even_min = num
                break
        for i in range(len(res)-1, -1, -1):
            if res[i] % 2 == 1:
                odd_max = res[i]
                break
        return odd_max - even_min