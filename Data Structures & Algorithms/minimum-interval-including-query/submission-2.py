class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # elms in intervals are [left_i, right_i] inclusive
        # given an arr of query points, the result of query[j] is the length of the shortest interval i that contains
        # the query.
        
        intervals.sort()
        org_idx = {}
        m = len(intervals)
        n = len(queries)

        for idx in range(n):
            query = queries[idx]
            if query not in org_idx:
                org_idx[query] = []
            org_idx[query].append(idx)
            

        queries.sort()

        # elms are (end_val, size)
        heap = []

        res = [-1] * n
        ptr = 0

        minSizes = {}

        for query in queries:
            print(query)
            while ptr < m and intervals[ptr][0] <= query:
                end = intervals[ptr][1]
                size = intervals[ptr][1] - intervals[ptr][0] + 1
                print(f"Pushing onto heap: ({size}, {end})")
                heapq.heappush(heap, (size, end))
                ptr += 1
            
            while heap and heap[0][1] < query:
                print(f"Popping from heap: {heap[0]}")
                heapq.heappop(heap)
            
            if heap:
                minSizes[query] = heap[0][0]
                print(f"Setting {query} to {heap[0][0]}")
            
        for query, indicies in org_idx.items():
            if query not in minSizes:
                continue
            for idx in indicies:
                res[idx] = minSizes[query]
        
        return res
            



