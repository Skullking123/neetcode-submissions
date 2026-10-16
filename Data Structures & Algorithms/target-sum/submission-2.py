class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Given an array of integers nums and an integer target
        # For each num in the arr, you can either choose to add or subtract it to a total sum
        # Return the number of different ways that you can build the expression such that the total sum equals target
        
        # This is knapsack. We are essentially sifting through possible partitions where the diff
        # between the sums of the two partitions is target
        s = sum(nums)
        
        # impossible
        if target < -s or target > s:
            return 0
        
        dp = [[0] * (s * 2 + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for row in range(1, len(dp)):
            # print(f"Adding or subtracting: {nums[row - 1]}")
            for col in range(len(dp[0])):
                
                psum = col
                if col > s:
                    psum -= s * 2 + 1
                addTo = psum - nums[row - 1]
                # default case if addTo < -s 
                addCount = 0 
                if addTo >= -s:
                    addCount = dp[row - 1][addTo]
                subFrom = psum + nums[row - 1]
                # default case if subFrom > s
                subCount = 0
                if subFrom <= s:
                    subCount = dp[row - 1][subFrom]
                
                dp[row][col] = addCount + subCount

        return dp[-1][target]
