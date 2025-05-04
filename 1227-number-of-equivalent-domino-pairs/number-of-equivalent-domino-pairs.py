class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num_of_pairs = 0
        store_dominoes = defaultdict(int)

        for a,b in dominoes:
            if a > b:
                a, b = b,a
            num_of_pairs += store_dominoes[(a,b)]
            store_dominoes[(a,b)] += 1
        return num_of_pairs