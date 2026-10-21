class Solution:
    def minSwaps(self, nums):
        length = len(nums)
        def sum_of_digits(n):
            sum = 0
            while(n>0):
                sum += n%10
                n //= 10
            return sum
        vp = []
        for i in range(length):
            vp.append([sum_of_digits(nums[i]), nums[i]])
        vp.sort()
        res = []
        for i in range(length):
            res.append(vp[i][1])

        temp = res
        
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        
        swaps = 0
        for i in range(len(nums)):
            if temp[i] != nums[i]:
                
                ind = pos[temp[i]]
                nums[i], nums[ind] = nums[ind], nums[i]

                pos[nums[i]] = i
                pos[nums[ind]] = ind
    
                swaps += 1
        return swaps
