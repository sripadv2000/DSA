class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in range(len(nums)):
            if nums[i] in store:
                return True
            store.add(nums[i])
        return False