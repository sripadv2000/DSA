class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_lis = text.split(" ")
        res = len(text_lis)
        for t in text_lis:
            for c in brokenLetters:
                if c in t:
                    res -= 1
                    break
        return res