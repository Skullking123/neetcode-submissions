import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = [] # stores tuples where the first element is the submax and the second is the idx of where the submax is

        # store inside heap the indexes that contain the biggest element within the subwindow
        # the top most element in the heap is the "earliest" elm in our window
        # check that the top most element is still in our window
        # pop if it is not and the next element should be the biggest element in the next window

        # jumpstart the heap, fills the heap with the elements of the init window
        for idx in range(k):
            heapq.heappush(heap, (nums[idx] * -1, idx))

        for start in range(len(nums) - k + 1):
            if start + k - 1 < len(nums):
                heapq.heappush(heap, (nums[start + k - 1] * -1, start + k - 1))
            while heap[0][1] < start:
                heapq.heappop(heap)

            res.append(heap[0][0] * -1)
            
        
        
        return res