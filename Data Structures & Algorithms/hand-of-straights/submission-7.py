class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        nog = len(hand) // groupSize # Number of Groups
        dic = defaultdict(int)
        for h in hand:
            dic[h] += 1
        heap = list(dic.keys())
        heapq.heapify(heap)
    
        while heap:
            last_item = heap[0]
            if dic[last_item] == 0:
                heapq.heappop(heap)
                continue
            dic[last_item] -= 1
            size = groupSize - 1
            while size > 0:
                last_item += 1
                if dic[last_item] == 0:
                    return False
                dic[last_item] -= 1
                size -= 1
        return True
            




        