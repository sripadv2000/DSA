class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0]*length

        answer[0] = 1

        for i in range(1, length):
            answer[i] = answer[i-1]*nums[i-1]
        
        r = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i]*r
            r = nums[i]*r
        
        return answer