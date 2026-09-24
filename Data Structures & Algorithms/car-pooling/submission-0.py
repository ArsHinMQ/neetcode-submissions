class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        passengers = 0
        heap = []
        for num, frm, to in trips:
            while heap and heap[0][0] <= frm:
                _, pnum = heapq.heappop(heap)
                passengers -= pnum
            if num + passengers > capacity:
                return False
            heapq.heappush(heap, (to, num))
            passengers += num
        return True