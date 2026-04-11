from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        map = defaultdict(list)

        for idx, num in enumerate(nums):
            map[num].append(idx)

        mini = 2*n

        for temp in map.values():
            m = len(temp)
            if m >= 3:
                for i in range(m-2):
                    mini = min(2*(temp[i+2]-temp[i]), mini)
        return -1 if mini == 2*n else mini
