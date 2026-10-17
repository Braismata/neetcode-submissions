"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==1: return True
        ocupado=set()
        while intervals:
            for num_ocupados in range(intervals[0].start,intervals[0].end):
                if num_ocupados in ocupado:return False
                ocupado.add(num_ocupados)
            intervals.pop(0)
        return True