"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""





class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalsAsLists = []
        for interval in intervals:
            intervalsAsLists.append([interval.start, interval.end])
        
        intervalsAsLists.sort()

        for idx in range(1, len(intervalsAsLists)):
            if intervalsAsLists[idx][0] < intervalsAsLists[idx - 1][1]:
                return False
        
        return True