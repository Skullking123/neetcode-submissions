"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = []

        for interval in intervals:
            sorted_intervals.append((interval.start, interval.end))
        
        sorted_intervals.sort()

        rooms = []

        for cs, ce in sorted_intervals:
            if rooms and rooms[0] <= cs:
                heapq.heappop(rooms)
                heapq.heappush(rooms, ce)
            else:
                heapq.heappush(rooms, ce)
        
        return len(rooms)