"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals_lst = []
        for intv in intervals:
            intervals_lst.append((intv.start, intv.end))
        intervals_lst.sort()
        maxi = intervals_lst[0][-1]
        for i in range(1, len(intervals_lst)):
            start, end = intervals_lst[i]
            if start < maxi:
                return False
            maxi = max(end, maxi)
        return True
