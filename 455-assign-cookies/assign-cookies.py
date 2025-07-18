class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        match = 0
        i, j = 0, 0

        while i<len(g) and j<len(s):
            if g[i] <= s[j]:
                match += 1
                i += 1
                j += 1
            else:
                j += 1
        return match