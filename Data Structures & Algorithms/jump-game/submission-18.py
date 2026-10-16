class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Given an int arr where each elm num[i] is the max jump len at that position
        # return true if you can reach the last index from 0, false otherwise
        
        n = len(nums)
        goal = n - 1

        for idx in range(n - 2, -1, -1):
            if nums[idx] + idx >= goal:
                goal = idx
        
        return goal == 0





        # THIS IS NOT EFFICIENT O(n^2 * log(n)): YOU ARE STILL ESSENTIALLY ITERATING OVER ALL POSSIBLE PATHS
        # THIS IS NOT GREEDY
        # we can start backwards, iterate in reverse from index n - 2
        # going backwards, we keep track of the paths that can reach index n - 1 (store their len and the idx they start at)
        # for ex: [5,0,2,0,0,1,0]
        # starting from n - 1 (idx 5), we would have (5, 1) since it starts at 5 and the path is 1 
        # when we reach the 2, we don't store anything else since we can't make a path with it
        # when we get to the 5 we would have (0, 6) (we popped (5, 1) and used it to calculate (0, 6))
            # because we are able to jump to idx 5 from idx 0 since we have a jump len of 5, we can use the path append that path to this
            # one
        # we return true because we have a path to idx 6 that starts at 0
        # we possibly store the paths in a heap, using the starting idx as our primary key to get O(1) lookup

        # heap = []
        # n = len(nums)
        # target = n - 1

        # if n == 1:
        #     return True

        # for idx in range(n - 2, -1, -1):
        #     if nums[idx] == 0:
        #         continue
            
        #     paths = []
        #     while heap and heap[0][0] <= nums[idx] + idx:
        #         start_idx, path_len = heapq.heappop(heap)
        #         paths.append((idx, path_len + (start_idx - idx)))
            
        #     for path in paths:
        #         heapq.heappush(heap, path)

        #     # if we are able to reach the target directly from idx
        #     print(nums[idx] + idx)
        #     print(target)
        #     if nums[idx] + idx >= target:
        #         heapq.heappush(heap, (idx, nums[idx]))
        
        # we only have paths that lead to target: n - 1
        # so if there is a path that starts at 0, it would be
        # at the top of the heap
        # if heap and heap[0][0] == 0:
        #     return True
        # else:
        #     return False


        # Doesn't work because going for the position with the biggest jump possible doesn't gurantee 
        # that you find the path to the last idx from 0:
        # See ex: [1,2,0,1,5,0,2,0,0,1,0]
        # pos: 0
        # pos: 1
        # pos: 3
        # pos: 4
        # pos: 6 # goes to the 5 instead of last 1
        # prev = 0
        # pos = 0
        # n = len(nums)
        # last = n - 1
        
        # if n == 1:
        #     return True

        # while pos < last and nums[pos] > 0:
        #     print(f"pos: {pos}")
        #     max_jump_len = nums[pos]

        #     if pos + max_jump_len >= last:
        #         return True

        #     # find the next place to jump to 
        #     largest_jump = float('-inf')
        #     idx = pos + 1
        #     # exclusive limit
        #     limit = pos + max_jump_len 
        #     # find the next 
        #     while idx < n and idx <= limit:
        #         # print(f"idx: {idx}")
        #         if nums[idx] >= largest_jump:
        #             pos = idx
        #             largest_jump = nums[idx] 
        #             # print(f"Jumping to {pos}")         
        #         idx += 1 
            
        # return False
