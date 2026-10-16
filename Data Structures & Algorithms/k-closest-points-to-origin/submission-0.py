class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # given a 2-d array where each row is a different (x, y) cord
        # return the k closest points to the origin (0, 0)

        # use a min-heap
        # the elms of the min-heap will be (dist, idx)

        # add all elms to the heap
        heap = []
        for idx in range(len(points)):
            x = points[idx][0]
            y = points[idx][1]
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), idx))
        
        res = []
        for _ in range(k):
            point = points[heapq.heappop(heap)[1]]
            res.append(point)
        
        return res 