class Solution:
    def check(self, nums: List[int]) -> bool:
        step = 0
        N=len(nums)
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                step += 1
        if nums[0] < nums[N-1]:
            step += 1
        return True if step <= 1 else False

# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         N = len(nums)
#         if N == 1:
#             return True
#         flag = 0
#         for i in range(N-1):
#             if nums[i] > nums[i+1]:
#                 flag += 1
        
#         if nums[0] < nums[N-1]:
#             flag += 1
#         return flag <= 1