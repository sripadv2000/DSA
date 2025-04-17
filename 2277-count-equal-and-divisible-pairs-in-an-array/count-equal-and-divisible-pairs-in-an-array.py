class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        num_of_pairs = 0
        dict = {} 

        for i in range(0, N):
            if nums[i] not in dict:
                dict[nums[i]] = [i]
            else:
                for j in range(len(dict[nums[i]])):
                    if i*dict[nums[i]][j] % k == 0:
                        num_of_pairs += 1
                dict[nums[i]].append(i)
        return num_of_pairs