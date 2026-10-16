class MedianFinder:

    def __init__(self):
        self.bot_half = [] # max-heap
        self.top_half = [] # min-heap

    def addNum(self, num: int) -> None:
        # base case
        print(f"adding: {num}")
        if len(self.top_half) == 0:
            heapq.heappush(self.top_half, num)
            return
        
        heapq.heappush(self.bot_half, -num)
        # print(f"Adding {num}")
        # print(f"Len of bot: {len(self.bot_half)}")
        # print(f"Len of top: {len(self.top_half)}")
        # print(self.bot_half)
        # print(self.top_half)
        # we need to rebalance the the two heaps to maintain:
        # maintain roughly same size:
            # if even, both same size
            # if odd, top 1 extra elm
        # no numerical overlap between the elms of both heaps
        offset = (len(self.bot_half) + len(self.top_half)) % 2

        # ensure no overlap
        # the smallest elm should not be smaller than the biggest elm in bot_half
        while self.top_half and -self.bot_half[0] > self.top_half[0]:
            elm = -heapq.heappop(self.top_half)
            heapq.heappush(self.bot_half, elm)

        print(sorted(self.bot_half))
        print(sorted(self.top_half))        
        # ensure that they're roughly the same size
        # here the only possibiliy is that bot_half is bigger or same size
        while len(self.bot_half) + offset > len(self.top_half):
            elm = -heapq.heappop(self.bot_half)
            heapq.heappush(self.top_half, elm)
        
        print(sorted(self.bot_half))
        print(sorted(self.top_half))


        


    def findMedian(self) -> float:
        if (len(self.bot_half) + len(self.top_half)) % 2 == 0:
            bot_med = -self.bot_half[0]
            top_med = self.top_half[0]
            return (bot_med + top_med) / 2
        else:
            return self.top_half[0]
        