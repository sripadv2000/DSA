class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        maxi = float('-inf')
        for i in range(n - 1, n - k - 1, -1):
            ans = 0
            for j in range(i, -1, -k):
                ans += energy[j]
                maxi = max(maxi, ans)
        return maxi

        
        