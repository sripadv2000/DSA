class Solution:

    def __init__(self, w: List[int]):
        self.running_sums = []
        total = 0

        for weight in w:
            total += weight
            self.running_sums.append(total)

        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        low, high = 0, len(self.running_sums)

        while low < high:
            mid = low + (high - low) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else:
                high = mid

        return low