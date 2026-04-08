class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If total cards can't be divided evenly, return False
        if len(hand) % groupSize != 0:
            return False

        # Store the frequency of each card
        freq = Counter(hand)

        # Use a min heap to always get the smallest available card
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        # Loop until all groups are formed
        while minHeap:
            # Start from the smallest card available
            first = minHeap[0]

            # Form a group starting from this card
            for i in range(groupSize):
                card = first + i

                # If card not in freq or frequency is 0, return False
                if freq[card] == 0:
                    return False

                # Decrease frequency
                freq[card] -= 1

                # If frequency is 0 and it's the top of the heap, pop it
                if freq[card] == 0 and card == minHeap[0]:
                    heapq.heappop(minHeap)

        # All groups formed successfully
        return True