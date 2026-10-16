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

        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        heap = []
        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
                continue
            
            if heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))

        res = []
        for _, num in heap:
            res.append(num)
        
        return res