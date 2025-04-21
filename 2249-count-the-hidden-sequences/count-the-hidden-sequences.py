class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mn, mx = 0, 0
        curr = 0

        for x in differences:
            curr += x
            mn = min(mn, curr)
            mx = max(mx, curr)
        
        return max((upper - lower + 1) - (mx - mn) , 0)