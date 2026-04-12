from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)
        minheap = list(freq.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for i in range(groupSize):
                card = first + i
                if freq[card] == 0:
                    return False
                freq[card] -= 1
                if freq[card] == 0 and card == minheap[0]:
                    heapq.heappop(minheap)
        return True