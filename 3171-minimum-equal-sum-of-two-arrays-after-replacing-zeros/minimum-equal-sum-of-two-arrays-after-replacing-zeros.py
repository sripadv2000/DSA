class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sums1, sums2, cnt1, cnt2 = 0, 0, 0, 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                sums1 += 1
                cnt1 += 1
            else:
                sums1 += nums1[i]

        for i in range(len(nums2)):
            if nums2[i] == 0:
                sums2 += 1
                cnt2 += 1
            else:
                sums2 += nums2[i]
        if sums1 < sums2 and cnt1 == 0:
            return -1
        if sums2 < sums1 and cnt2 == 0:
            return -1
        return max(sums1, sums2)
        