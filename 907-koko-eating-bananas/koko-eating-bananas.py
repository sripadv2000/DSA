class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_hours(arr, rate):
            hours = 0
            for i in range(len(arr)):
                if arr[i]%rate == 0:
                    hours += arr[i]//rate
                else:
                    hours += arr[i]//rate + 1
            return hours

        l, r = 1, max(piles)

        while l <= r:
            mid = (l+r)//2
            no_of_hours = find_hours(piles, mid)
            if no_of_hours > h:
                l = mid + 1
            else:
                r = mid - 1
        return l