from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp = defaultdict(int)
        result = 0

        for word in words:
            reversed_word = word[::-1]

            if mp[reversed_word] > 0:
                result += 4
                mp[reversed_word] -= 1
            else:
                mp[word] += 1

        for word, count in mp.items():
            if word[0] == word[1] and count > 0:
                result += 2
                break

        return result
