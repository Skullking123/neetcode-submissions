class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # given an arr nums, and and int k
        # split nums into k non-empty subarrs such that the largest sum of any subarr is minimized

        # first idea:
        # we split the array into k groups that are roughly equal in length
        # we could then move the bounds of each subarr
        # maintain a hashmap to map each subarr to their bounds and current sum
        # when we elongate a subarr, we need to add to the elongated subarr and sub from the shrunken subarr

        # ex: [2,4,10,1,5]  k = 2
        # [2, 4], [10, 1, 5] largest = 16
        # We can elongate [2,4]: [2, 4, 10], [1, 5] largest is still 16
        # We cannot elongate [2, 4, 10] to [2, 4, 10, 1] as it will exceed our current largest of 16


        # ex: [1, 0, 2, 3, 5] k = 4
        # [1], [0], [2], [3, 5] largest = 8
        # We can shrink [3, 5] to get: [1], [0], [2,3], [5] largest is now 5
        # We can look at [5] and [2, 3]:
            # We can't do anything with [5] since elongating it increases our largest and we can't make a subarr empty
            # We must look at [2, 3] and can only shrink it 
        # we get [1], [0, 2], [3], [5] largest is still 5
        # we can also elongate [1] to [1, 0] to give us: [1, 0], [2], [3], [5] 

        # at every step we are looking to shrink the subarr with the largest sum
            # we should only shrink a subarr if it has more than one elm
        # [0,10,15,20] k = 3
        # [0, 1, 2, 3]
        # [0], [10], [15, 20]
        # [0], [10, 15], [20]        
        # [0, 10], [15] [20]
        # [0, 1, 2, 3, 4, 5] k = 3
        mem = {}
        def dfs(idx, partition):
            # don't repeat computations
            if (idx, partition) in mem:
                return mem[(idx, partition)]

            if partition == 1:

                res = sum(nums[idx:])
                mem[(idx, partition)] = res
                # print(idx, partition, res)
                return res

            prefix = 0
            res = float("inf")
            for nIdx in range(idx,  len(nums) - partition + 1):
                # elongate the current subarr
                prefix += nums[nIdx]
                # compute minimum largest sum for the rest of the list
                suffixMax = dfs(nIdx + 1, partition - 1)
                largestSum = max(prefix, suffixMax)
                res = min(res, largestSum)
            
            # print(idx, partition, res)
            mem[(idx, partition)] = res
            return res
        
        return dfs(0, k)



        









