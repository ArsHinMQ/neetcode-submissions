class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        counter = 0
        maxi = intervals[0][1]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a < maxi or b < maxi:
                counter += 1
                maxi = min(b, maxi)
            else:
                maxi = b
        return counter