class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        n = len(s)
        for idx in range(n):
            letter = s[idx]
            if letter not in intervals:
                intervals[letter] = [idx, idx]
            intervals[letter][1] = idx
        
        if len(intervals) == 1:
            return [s]
       
        merged = []
        intervals = list(intervals.values())
        merged.append(intervals[0])
        for start, end in intervals[1:]:
            if start < merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], end)]
            else:
                merged.append([start, end])
        return list(map(lambda x: x[1] - x[0] + 1, merged))