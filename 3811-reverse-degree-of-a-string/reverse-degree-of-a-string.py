class Solution:
    def reverseDegree(self, s: str) -> int:
        degree_arr = []
        reverse_degree = 0

        for i in range(26, 0, -1):
            degree_arr.append(i)

        for i in range(len(s)):
            reverse_degree += degree_arr[(ord(s[i]) - 97)] * (i+1)
        return reverse_degree