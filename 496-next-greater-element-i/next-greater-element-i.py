class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2  = len(nums1), len(nums2)
        def NGR(arr, n2):
            res = [-1]*n2
            stack = []
            for i in range(n2-1,-1,-1):
                while stack and arr[i] >= stack[-1]:
                    stack.pop()
                    
                if stack:
                    res[i] = stack[-1]
                stack.append(arr[i])
            return res

        ngr = NGR(nums2, n2)

        dict = {}
        for i in range(n2):
            dict[nums2[i]] = ngr[i]
        # Map nums2 values to their NGR result for O(1) access
        # mapping = {nums2[i]: ngr[i] for i in range(n2)}
        
        res = []
        for num in nums1:
            res.append(dict[num])
        return res
        # # Build the final result based on nums1
        # return [mapping[val] for val in nums1]
