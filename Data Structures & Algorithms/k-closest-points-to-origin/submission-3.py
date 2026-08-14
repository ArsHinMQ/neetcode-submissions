class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for p in points:
            x, y = p
            diff = -(math.sqrt((0 - x) ** 2 + (0 - y) ** 2))
            heapq.heappush(heap, (diff, p))
            if len(heap) > k:
                heapq.heappop(heap)


        res = []
        for item in heap:
            _, p = item
            res.append(p)
        
        return res
