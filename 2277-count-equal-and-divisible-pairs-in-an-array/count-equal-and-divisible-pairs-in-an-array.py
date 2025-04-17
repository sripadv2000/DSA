class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        num_of_pairs = 0

        for i in range(0, N-1):
            for j in range(i+1, N):
                if nums[i]==nums[j] and (i*j)%k == 0:
                    num_of_pairs += 1
        return num_of_pairs