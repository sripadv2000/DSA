class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def count_digits(num):
            count_of_digits = 0
            while(num):
                count_of_digits += 1
                num = num//10
            return count_of_digits

        cnt = 0
        for num in nums:
            if count_digits(num) % 2 == 0:
                cnt += 1
        return cnt