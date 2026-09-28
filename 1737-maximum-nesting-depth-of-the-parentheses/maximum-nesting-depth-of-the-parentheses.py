class Solution:
    def maxDepth(self, s: str) -> int:
        current = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                current += 1
            elif s[i] == ")":
                current -= 1
            depth = max(depth, current)
        return depth