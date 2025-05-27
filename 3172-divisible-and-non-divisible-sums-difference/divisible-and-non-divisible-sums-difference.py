class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_divisible = 0
        divisible = 0

        for num in range(1, n+1):
            if num % m == 0:
                divisible += num
            else:
                not_divisible += num

        return (not_divisible - divisible)