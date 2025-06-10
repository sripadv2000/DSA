from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)
        for char in s:
            hashMap[char] += 1
        for char in t:
            hashMap[char] -= 1

        for key, val in hashMap.items():
            if val != 0:
                return False
        
        return True