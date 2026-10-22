class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Given an arr of distinct integers nums and an integer target
        # Return the number of possible permutations with replacement that add up 
        # to target 
        
        # n = len(nums)
        # m = target
        # Runtime complexity: O(m * n)
        # Space complexity: O(m) 

        nums.sort()

        p_sum = {}
        def dfs(c_sum):
            # don't repeat computations
            if c_sum in p_sum:
                return p_sum[c_sum]
            # base cases
            elif c_sum == 0:
                return 1
            
            num_permute = 0
            for num in nums:
                if c_sum - num < 0:
                    break
                num_permute += dfs(c_sum - num)
            
            p_sum[c_sum] = num_permute
            return num_permute
        
        return dfs(target)
            