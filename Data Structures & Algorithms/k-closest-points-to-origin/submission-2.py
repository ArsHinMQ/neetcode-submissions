class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p
            diff = abs(math.sqrt((0 - x) ** 2 + (0 - y) ** 2))
            heap.append((diff, p))

        heapq.heapify(heap)

        res = []
        while k > 0:
            k -= 1
            _, p = heapq.heappop(heap)
            res.append(p)
        return res
