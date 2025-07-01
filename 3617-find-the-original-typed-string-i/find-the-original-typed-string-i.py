class Solution:
    def possibleStringCount(self, word: str) -> int:
        l, r = 0,0
        N = len(word)

        groups = 1

        while(l<N and r<N):
            if word[r] == word[l]:
                r += 1
            else:
                l = r
                groups += 1
        return N - groups + 1
