class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
# print(ord('a')) -> 97
# print(ord('z')) -> 122
# print(ord('A')) -> 65
# print(ord('Z')) -> 90
        arr = [0]*52
        for char in word:
            num = ord(char)
            if char.isupper():
                arr[num - 65] += 1
            else:
                arr[num - 97 + 26] += 1
        
        res = 0
        for i in range(26):
            if arr[i] > 0 and arr[i + 26] > 0:
                res += 1
        
        return res
                