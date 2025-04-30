class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if (10 <= num <= 99) or (1000 <= num <= 9999) or (num == 100000):
                cnt += 1
        return cnt