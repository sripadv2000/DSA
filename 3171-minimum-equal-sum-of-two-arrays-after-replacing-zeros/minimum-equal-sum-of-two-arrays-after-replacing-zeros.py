class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sums1, sums2, cnt1, cnt2 = 0, 0, 0, 0
        for num in nums1:
            sums1 += num
            if num == 0:
                cnt1 += 1
                sums1 += 1

        for num in nums2:
            sums2 += num
            if num == 0:
                cnt2 += 1
                sums2 += 1

        if (cnt1 == 0 and sums1 < sums2) or (cnt2 == 0 and sums2 < sums1):
            return -1
        return max(sums1, sums2)
        