class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            for char in word:
                if ord(char) < 122:
                    word += chr(ord(char)+1)
                else:
                    word += chr(ord('a'))

        return word[k-1]