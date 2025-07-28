class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        count = 0
        for i in range(1, len(filtered) - 1):
            prev, curr, next_ = filtered[i - 1], filtered[i], filtered[i + 1]

            if (prev < curr > next_) or (prev > curr < next_):
                count += 1

        return count