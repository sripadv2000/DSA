# choose any random number, swap it with last element in array and pop the last element
import random

class Solution:
    def __init__(self, nums):
        self.nums = nums[:]

    def reset(self):
        return self.nums[:]

    def shuffle(self):
        temp = self.nums[:]
        result = []

        while temp:
            r = random.randrange(len(temp))
            result.append(temp[r])
            temp[r], temp[-1] = temp[-1], temp[r]
            temp.pop()
        return result