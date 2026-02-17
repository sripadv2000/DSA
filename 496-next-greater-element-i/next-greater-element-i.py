class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def NGR(arr):
            n = len(arr)
            res = [-1]*n
            for i in range(n):
                for j in range(i+1, n):
                    if arr[j]>arr[i]:
                        res[i]=arr[j]
                        break
            return res

        ngr = NGR(nums2)
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    result.append(ngr[j])
        return result
