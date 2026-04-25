"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        intervals_length = len(intervals)
        index = 0
        while index < intervals_length - 1:
            if intervals[index].end > intervals[index+1].start:
                return False
            index += 1
        return True
            

