class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # given an arr of intervals [start, end], return the minimum number of interval;s you need to remove 
        # the rest of the intervals non-overlapping

        # what we can do is instead figure whats the maximum number of intervals
        # that we can use to determinine the minimum number of intervals that we need to
        # remove

        # elms are intervals but reversed so: [end, start]
        heap = [] 
        # time = float('inf')    
        for interval in intervals:
            heapq.heappush(heap, [interval[1], interval[0]])
            # time = min(time, interval[0])
        
        count = 0
        while heap:
            end, start = heapq.heappop(heap)
            while heap and heap[0][1] < end:
                heapq.heappop(heap)
                count += 1
            
        return count
        
        # [[-73,-26],[-65,-11],[-63,2],[-62,-49],[-52,31],[-40,-26],[-31,49],[30,47],[58,95],[66,98],[82,97],[95,99]]
    