class Solution:
    def numberOfSpecialChars(self, word):
        dict = {}
        res = 0
        
        for i in range(len(word)):
            if word[i].islower():
                dict[word[i]] = i
            elif word[i].isupper() and word[i] not in dict:
                dict[word[i]] = i
        
        st = set(word)
        
        for char in st:
            if char.islower() and char.upper() in st and dict[char.upper()] > dict[char]:
                res += 1
        return res