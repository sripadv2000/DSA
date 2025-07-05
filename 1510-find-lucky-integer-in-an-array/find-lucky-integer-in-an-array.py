class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0]*501
        freq[0] = -1

        for n in arr:
            freq[n] += 1
            
        for i in range(len(arr), -1, -1):
            if freq[i] == i:
                return i
        return -1