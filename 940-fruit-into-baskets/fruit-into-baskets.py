class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i, j = 0, 0
        count = 0
        mp = defaultdict(int)

        while j<n:
            mp[fruits[j]] += 1
            if len(mp) <= 2:
                count  = max(count, j-i+1)
            else:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1
            j += 1
        return count
