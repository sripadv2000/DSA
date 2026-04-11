class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent) 
        dp = [0]*n 
        res = 0 
        count = defaultdict(int) 
        for i in range(n): 
            mask = self.bit(dp, parent, s, i) 
            v = count[mask] 
            for j in range(26): 
                res += count[mask ^ (1 << j)] 
            res += v 
            count[mask] += 1 
        return res 

    def bit(self, dp, parent, s, i): 
        if i > 0 and dp[i] == 0: 
            dp[i] = self.bit(dp, parent, s, parent[i]) ^ (1 << (ord(s[i]) - ord('a'))) 
        return dp[i]