class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        zero_pointer = 0
        two_pointer = N - 1

        curr_pointer = 0
        while curr_pointer <= two_pointer:
            if nums[curr_pointer] == 0:
                nums[curr_pointer], nums[zero_pointer] = nums[zero_pointer], nums[curr_pointer]
                zero_pointer += 1
                curr_pointer += 1
            elif nums[curr_pointer] == 1:
                curr_pointer += 1
            elif nums[curr_pointer] == 2:
                nums[curr_pointer], nums[two_pointer] = nums[two_pointer], nums[curr_pointer]
                two_pointer -= 1