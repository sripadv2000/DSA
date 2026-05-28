class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        length = len(strs[0])

        for i in range(length):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res