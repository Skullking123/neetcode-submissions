class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # given a 2-d array where each row is a different (x, y) cord
        # return the k closest points to the origin (0, 0)

        # use a min-heap
        # the elms of the min-heap will be (dist, idx)

        # max-heap, keep the heap to size of k
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _, point in heap:
            res.append(point)
        
        return res 