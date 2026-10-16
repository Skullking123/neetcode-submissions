class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an arr of nums and a int k, return the k most frequent elms in the arr
        # get counts of all numbers first
        # then iterate through the counts inserting into a min-heap
            # always maintain at max k elms in the min-heap
            # whenever evaluating a count, look at the smallest elm in the heap
                # if the count is bigger than the smallest count in the heap, pop from the heap and push the count
                # otherwise continue
        # then unflatten the heap to only contain the actual elms

        heap =  [] # (counts, elm)

        # get the counts of every elm in nums
        counts = {}
        for elm in nums:
            if elm not in counts:
                counts[elm] = 0
            counts[elm] += 1
        
        # print(counts)
        # start pushing onto the heap. Keep the size of the heap at k
        for elm, count in counts.items():
            heapq.heappush(heap, (count, elm))

            if len(heap) > k:
                heapq.heappop(heap)
            
            # print(heap)
        
        res = []
        for _, elm in heap:
            res.append(elm)
        
        return res