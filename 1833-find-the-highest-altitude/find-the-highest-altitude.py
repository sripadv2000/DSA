class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        high = cur

        for alt in gain:
            cur += alt
            high = max(high, cur)
        
        return high