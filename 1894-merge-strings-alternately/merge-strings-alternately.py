class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        w1, w2 = len(word1), len(word2)
        while i < w1 and i < w2:
            res += word1[i]
            res += word2[i]
            i += 1
        while i < w1:
            res += word1[i]
            i += 1
        while i < w2:
            res += word2[i]
            i += 1
        return res