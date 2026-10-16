class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # given an arr of integers called nums, nums[i] = value of the ith balloon
        # you must burst all the balloons
        # If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1 coins]. 
            # If i - 1 or i + 1 go out of bounds, then assume they are 1
        
        # Return the maximum number of coins you can recieve by bursting all of the balloons
        
        # [4,2,3,7] --> [4,2,7] --> [4,7] --> [7]
        # 2*3*7      +    4*2*7  +   1*4*7  +  7  = 133

        # [1,2,3]
        # Possibilities:
        # [1,2,3] --> [1,3] --> [3]
        #  1*2*3   +  1*1*3  +   1*3*1 = 12
        # [1,2,3] --> [1,3] --> [1]
        #  1*2*3   +   1*3*1 +   1*1*1 = 10
        # [1,2,3] --> [2,3] --> [3]
        #  1*1*2   +  1*2*3 +  1*3*1 = 11
        # [1,2,3] --> [2,3] --> [2]
        #  1*1*2   +  2*3*1  + 1*2*1 = 10
        # [1,2,3] --> [1,2] --> [2]
        #  2*3*1   +  1*1*2  + 1*2*1 = 10
        # [1,2,3] --> [1,2] --> [1]
        #  2*3*1   +  1*2*1  + 1*1*1 = 9
        
        mem = {}

        def dfs(nums):
            if len(nums) == 1:
                return nums[0]

            if tuple(nums) in mem:
                return mem[tuple(nums)]

            res = 0
            for idx in range(len(nums)):
                # burst this balloon now 
                left = nums[idx - 1] if idx - 1 >= 0 else 1
                right = nums[idx + 1] if idx + 1 < len(nums) else 1
                res = max(res, (left * nums[idx] * right) + dfs(nums[:idx] + nums[(idx + 1):]))               
            
            mem[tuple(nums)] = res
            return res
        
        return dfs(nums)












