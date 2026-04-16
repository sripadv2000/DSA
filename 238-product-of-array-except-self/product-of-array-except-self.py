class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix, suffix, answer = [0]*length, [0]*length, [0]*length

        prefix[0] = 1

        for i in range(1, length):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix[length - 1] = 1
        for i in range(length - 2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(length):
            answer[i] = prefix[i]*suffix[i]
        
        return answer