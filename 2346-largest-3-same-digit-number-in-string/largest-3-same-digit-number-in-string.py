class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = str(num)
        ans = ""
        for i in range(1, len(s)-1):
            if s[i-1]==s[i]==s[i+1]:
                if ans == "":
                    ans = s[i-1:i+2]
                elif ans[0] < s[i-1]:
                    ans = s[i-1:i+2]
        return ans