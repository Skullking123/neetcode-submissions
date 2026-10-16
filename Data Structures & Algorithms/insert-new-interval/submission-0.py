class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Given an arr of non-overlapping intervals [[start, end]] that is in ascending order by start
        # insert newInterval into intervals such that intervals is still sored in ascending order by start_i and does
        # not have any overlapping intervals
        # base case
        # if len(intervals) == 0:
        #     return [newInterval]

        newS, newE = newInterval

        res = []
        idx = 0
        while idx < len(intervals) and newS > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        
        res.append(newInterval)
        for restIdx in range(idx, len(intervals)):
            currS, currE = intervals[restIdx]
            if res[-1][1]  >= intervals[restIdx][0]:
                prevS, prevE = res[-1]
                res[-1] = [min(prevS, currS), max(prevE, currE)]
            else:
                res.append(intervals[restIdx])
        
        return res