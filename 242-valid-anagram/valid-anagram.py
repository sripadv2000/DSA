class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        s_len, t_len = len(s), len(t)
        
        if s_len != t_len:
            return False

        for i in range(s_len):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        return True