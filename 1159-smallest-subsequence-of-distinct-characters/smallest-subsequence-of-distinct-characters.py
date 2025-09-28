class Solution:
    def smallestSubsequence(self, s: str) -> str:
        N = len(s)
        res = ""
        taken = [0]*26
        last_index = [0]*26

        for i in range(N):
            last_index[ord(s[i]) - ord('a')] = i
        
        for i in range(N):
            ch = s[i]
            idx = ord(ch) - ord('a')

            if taken[idx] == 1:
                continue
            
            while len(res) > 0 and res[-1] > ch and last_index[ord(res[-1]) - ord('a')] > i:
                taken[ord(res[-1]) - ord('a')] = 0
                res = res[:-1]
            
            res += ch
            taken[idx] = 1
        return res