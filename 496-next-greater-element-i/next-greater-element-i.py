class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def NGR(arr):
            n = len(arr)
            res = [-1]*n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and arr[i] >= stack[-1]:
                    stack.pop()
                    
                if stack:
                    res[i] = stack[-1]
                stack.append(arr[i])
            return res

        ngr = NGR(nums2)
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    result.append(ngr[j])
        return result
