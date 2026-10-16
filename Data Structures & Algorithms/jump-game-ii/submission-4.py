class Solution:
    def jump(self, nums: List[int]) -> int:
        # Given an int arr where each elm num[i] is the max jump len at that position
        # return the minimum jumps needed to reach the last idx. Assume there is always a valid answer
        n = len(nums)
        l = 0
        r = 0
        res = 0
        while r < len(nums) - 1:
            # print(f"[{l}, {r}]")
            farthest = l
            for pos in range(l, r + 1):
                if pos + nums[pos] >= farthest:
                    farthest = pos + nums[pos]
            # print(f"farthest: {farthest}")
            res += 1
            l = r + 1
            r = farthest

        return res

        # previous solution doesn't necessarily work because it just looks for a path and 
        # not the most optimal path 
        # n = len(nums)
        # goal = n - 1
        # res = 0

        # for idx in range(n - 2, -1, -1):
        #     if nums[idx] + idx >= goal:
        #         goal = idx
        
        # return goal == 0
            

            
            
