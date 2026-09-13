"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        if not intervals:
            return 0

        counter = 0
        heap = []
        for intv in intervals:
            start, end = intv.start, intv.end
            if heap and heap[0] <= start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                counter += 1
                heapq.heappush(heap, end)
        return counter
        