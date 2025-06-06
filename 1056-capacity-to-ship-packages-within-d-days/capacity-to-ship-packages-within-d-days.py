class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(arr, cap):
            days = 1
            load = 0
            for i in range(len(arr)):
                if load+arr[i] > cap:
                    days += 1
                    load = arr[i]
                else:
                    load += arr[i]
            return days

        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l + (r-l)//2
            val = helper(weights, mid)
            if val <= days:
                r = mid - 1
            else:
                l = mid + 1
                
        return l