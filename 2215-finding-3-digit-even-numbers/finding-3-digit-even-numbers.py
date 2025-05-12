from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits_dict = Counter(digits)
        results = []

        for num in range(100, 1000, 2):
            num_digits = [int(d) for d in str(num)]
            num_dict = Counter(num_digits)

            if all(num_dict[d] <= digits_dict[d] for d in num_dict):
                results.append(num)
        return results