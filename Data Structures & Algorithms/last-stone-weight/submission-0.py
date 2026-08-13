class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = [-s for s in stones]
        heapq.heapify(stones_neg)

        while len(stones_neg) > 1:
            first = -(heapq.heappop(stones_neg))
            second = -(heapq.heappop(stones_neg))
            if first - second == 0:
                continue
            heapq.heappush(stones_neg, -(first - second)) 
        
        return -(stones_neg[0]) if len(stones_neg) > 0 else 0
        