class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given an arr of stones where the ith index is the weight of the ith stone
        # At each step we choose the two heviest stones with weight x and y
            # if x == y, both are destroyed
            # if x < y, then the stone of weight x is destroyed, and the stone of weight y has new weight y - x
        # continue the simulation until there is only one stone left
        # return the weight of the last stone. Return 0 if none are left 
        # use a max-heap, add all stones to the max-heap
            # since python only has a min-heap, we can just multiply by -1 to make the "bigger" elms appear
            # at the top of the tree
        
        # add all stones into the max-heap
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while heap:
            stone1 = heapq.heappop(heap)
            stone2 = 0
            if heap:
                stone2 = heapq.heappop(heap)
            else:
                # there is only one stone left
                return -stone1
            
            heapq.heappush(heap, abs(stone1 - stone2) * -1)

        return 0
