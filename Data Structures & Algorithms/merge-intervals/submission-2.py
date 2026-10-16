class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        for start, end in intervals:
            # start > prev_end
            prev = merged_intervals[-1] if merged_intervals else [0, 0]
            if start > prev[1]:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1] = [prev[0], max(end, prev[1])]

        return merged_intervals