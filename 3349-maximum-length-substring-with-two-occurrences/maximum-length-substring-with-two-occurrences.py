class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = {}
        l, max_len = 0, 0
        
        for r, char in enumerate(s):
            if char in char_count:
                char_count[char] += 1
                while char_count[char] > 2:
                    char_count[s[l]] -= 1
                    if char_count[s[l]] == 0:
                        del char_count[s[l]]
                    l += 1
            else:
                char_count[char] = 1
                
            if (r - l + 1) > max_len:
                max_len = (r - l + 1)
        
        return max_len