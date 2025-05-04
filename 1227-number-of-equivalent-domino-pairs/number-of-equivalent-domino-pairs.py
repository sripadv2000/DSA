class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num_of_pairs = 0
        store_dominoes = defaultdict(int)
        n = len(dominoes)

        for i in range(0, n):
            a, b = dominoes[i][0], dominoes[i][1]
            if a > b:
                a, b = dominoes[i][1], dominoes[i][0]
            store_dominoes[(a,b)] += 1
                
        for num in store_dominoes.values():
            num_of_pairs += num*(num-1) // 2
        return num_of_pairs