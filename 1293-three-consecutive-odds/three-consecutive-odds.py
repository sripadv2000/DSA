class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3:
            return False
        for i in range(1, len(arr)-1):
            if (arr[i-1] % 2) and (arr[i] % 2) and (arr[i+1] % 2):
                return True
        return False
