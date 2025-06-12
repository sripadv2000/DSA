class Solution:
    def partitionString(self, s: str) -> int:
        N = len(s)
        dict = {}
        res = 0

        for i in range(len(s)):
            if s[i] in dict:
                dict = {}
                dict[s[i]] = 1
                res += 1
            else:
                dict[s[i]] = 1
            
        return res+1