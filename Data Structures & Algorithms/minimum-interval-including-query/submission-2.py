class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        result = [0] * len(queries)
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort()

        prev = None
        j = 0
        heap = []
        for q, i in qs:
            while j < len(intervals):
                s, e = intervals[j]
                if s > q:
                    break
                heapq.heappush(heap, (e - s + 1, e))
                j += 1
            while heap:
                size, end = heap[0]
                if end < q:
                    heapq.heappop(heap)
                else:
                    result[i] = size
                    break
            else:
                result[i] = -1

        return result
            