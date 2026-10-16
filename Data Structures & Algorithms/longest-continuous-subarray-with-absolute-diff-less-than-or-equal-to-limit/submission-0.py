class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # return the size of the longest-non-empty subarray such that the biggest diff
        # between any two elms in the is <= limit

        # use a sliding window
        # keep track of min and max of our subarr when increasing or decreaseing the window
            # maintain both a min-heap and max-heap
            # elms in the heap would be (num, idx)
            # use idx to check if it is in our subarr
        # increase the size of subarr (add on right) when max - min <= limit
        # decrease the size of subarr (pop from left) when max - min > limit
        
        res = 0
        left = 0
        maxHeap = []
        minHeap = []
        for right in range(len(nums)):
            # add elm
            heapq.heappush(maxHeap, (nums[right] * -1, right))
            heapq.heappush(minHeap, (nums[right], right))

            # remove elms not in our subArr
            while maxHeap[0][1] < left:
                heapq.heappop(maxHeap)
            while minHeap[0][1] < left:
                heapq.heappop(minHeap)
            
            smallest = minHeap[0][0]
            biggest = maxHeap[0][0] * -1
            
            if biggest - smallest <= limit:
                res = max(res, right - left + 1)
            else: # when biggest - smallest > limit
                # decrease our window and pop from left
                while biggest - smallest > limit:
                    if left == maxHeap[0][1]:
                        heapq.heappop(maxHeap)
                        biggest = maxHeap[0][0] * -1
                    if left == minHeap[0][1]:
                        heapq.heappop(minHeap)
                        smallest = minHeap[0][0]

                    left += 1
            
        return res
            
