class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        dict = defaultdict(int)

        for num in range(1, n+1):
            sum_of_digits = 0
            temp = num
            while(temp > 0):
                sum_of_digits += temp%10
                temp = temp//10
            dict[sum_of_digits] += 1 
        
        max_value = max(dict.values())
        res = 0
        for val in dict.values():
            if val == max_value:
                res += 1
        return res