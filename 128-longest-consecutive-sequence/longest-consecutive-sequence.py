class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestLength = 0
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = False

        for num in nums:
            currLength = 1

            # Check in forward direction
            nextNum = num + 1
            while(nextNum in dict and dict[nextNum] == False):
                currLength += 1
                dict[nextNum] = True
                nextNum += 1
            
            # Check in reverse direction
            prevNum = num - 1
            while(prevNum in dict and dict[prevNum] == False):
                currLength += 1
                dict[prevNum] = True
                prevNum -= 1
            
            longestLength = max(longestLength, currLength)
        return longestLength
