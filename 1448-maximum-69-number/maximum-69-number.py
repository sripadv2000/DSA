class Solution:
    def maximum69Number (self, num: int) -> int:
        lis = list(str(num))

        for l in range(len(lis)):
            if lis[l] == "6":
                lis[l] = "9"
                break

        return int(''.join(lis))