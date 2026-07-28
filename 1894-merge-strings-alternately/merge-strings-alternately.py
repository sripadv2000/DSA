class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        w1, w2 = len(word1), len(word2)
        n = max(w1, w2)
        for i in range(n):
            if i < w1:
                res += word1[i]
            if i < w2:
                res += word2[i]
            i += 1
        return res