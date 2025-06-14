class Solution:
    def minMaxDifference(self, num: int) -> int:
        snum = str(num)
        i = 0
        for i in range(len(snum)):
            if snum[i] != "9":
                break
        maxi = int(snum.replace(snum[i],"9"))
        mini = int(snum.replace(snum[0],"0"))
        return maxi - mini