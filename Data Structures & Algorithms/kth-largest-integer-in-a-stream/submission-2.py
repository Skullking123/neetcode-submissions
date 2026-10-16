class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

             

    def add(self, val: int) -> int:
        # ignore values smaller than our current kth largest elm
        # when we add values bigger than our kth largest elm, evaluate what comes "next"
        # use a min heap to store what comes next?

        # get the next element largest element
        heapq.heappush(self.heap, val)
        if len(self.heap) <= self.k:
            return self.heap[0]
        else:
            heapq.heappop(self.heap)
            return self.heap[0]

            