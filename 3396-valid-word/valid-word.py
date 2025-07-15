class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel, consonant, no_special = False, False, True
        vowels = ['a', 'e', 'i', 'o', 'u']

        for chr in word:
            if not chr.isalnum():
                no_special = False
                break
    
            if chr.lower() in vowels:
                vowel = True
            elif chr.isalpha() and chr.lower not in vowels:
                consonant = True
        
        return no_special and vowel and consonant