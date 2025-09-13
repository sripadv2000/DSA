class Solution:
    def maxFreqSum(self, s: str) -> int:
        arr = [0]*26
        for c in s:
            arr[ord(c)-97] += 1
        
        vowel, consonant = 0, 0

        for i in range(26):
            if i == 0 or i== 4 or i==8 or i==14 or i==20:
                vowel = max(vowel, arr[i])
            else:
                consonant = max(consonant, arr[i])
        return (vowel + consonant)