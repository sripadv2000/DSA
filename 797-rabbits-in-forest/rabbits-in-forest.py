from math import ceil
from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        dict = defaultdict(int)
        for i in range(len(answers)):
            dict[answers[i]] += 1

        for key, val in dict.items():
            group = ceil(val/(key+1))
            res += group*(key+1)
        return res