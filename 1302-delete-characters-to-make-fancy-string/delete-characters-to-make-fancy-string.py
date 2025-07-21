class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if len(res) > 1 and res[-1]==s[i] and res[-2]==s[i]:
                continue
            res += s[i]
        return res