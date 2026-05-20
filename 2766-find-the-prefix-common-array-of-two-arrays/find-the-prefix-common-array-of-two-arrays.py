class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_arr = [0]*n
        freq = [0 for _ in range(n+1)]
        common_cnt = 0

        for cur_idx in range(n):
            freq[A[cur_idx]] += 1
            if freq[A[cur_idx]] == 2:
                common_cnt += 1
            
            freq[B[cur_idx]] += 1
            if freq[B[cur_idx]] == 2:
                common_cnt += 1
            
            prefix_arr[cur_idx] = common_cnt
            
        return prefix_arr
