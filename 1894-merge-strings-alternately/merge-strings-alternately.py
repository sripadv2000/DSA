class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        w1, w2 = len(word1), len(word2)
        n = min(w1, w2)
        for i in range(n):
            res += word1[i] + word2[i]
        
        if w1 < w2:
            res += word2[n:]
        else:
            res += word1[n:]

        return res