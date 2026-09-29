class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        curr = 0
        for i in range(len(s)):
            if s[i] == "(":
                curr += 1
            elif s[i] == ")":
                curr -= 1
            maximum = max(curr, maximum)
        return maximum