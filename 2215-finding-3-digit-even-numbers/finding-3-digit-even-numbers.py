class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result_set = set()

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                for k in range(n):
                    if i==k or j==k:
                        continue
                    a,b,c = digits[i], digits[j], digits[k]
                    if a==0:
                        continue
                    if c%2 != 0:
                        continue
                    number = a*100 + b*10 +c
                    result_set.add(number)
        return sorted(list(result_set))


            
        