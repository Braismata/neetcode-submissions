"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==1: return 1
        if len(intervals)==0: return 0
        ocupado={}
        maximo=1
        while intervals:
            for num_ocupados in range(intervals[0].start,intervals[0].end):
                if num_ocupados in ocupado:
                    ocupado[num_ocupados]+=1
                    if maximo<ocupado[num_ocupados]: maximo=ocupado[num_ocupados]
                else:
                    ocupado[num_ocupados]=1
            intervals.pop(0)
        return maximo