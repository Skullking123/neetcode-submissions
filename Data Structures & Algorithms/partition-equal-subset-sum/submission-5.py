class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return true if you can partition the arr into two subsets, where the sum of 
        # both subsets are equal. Return false otherwise

        # There are 2^n possible subsets. There are (2^n - 1) * (2^n - 2) possible combinations.
        # Subsets are composed of other subsets. You can build additional subsets by using other subsets

        # Since sum(subset1) == sum(subset2), and both are partitions of nums. Then sum(nums) == sum(subset1) + sum(subset2)
        # And since both are equal, sum(subset1) == sum(subset2) == sum(nums) / 2
        # the list cannot be partitioned if sum(nums) is odd
        # our target should be if we can make a partition that equals sum(nums) / 2
        # we approach this like knapsack, come up with a combination of numbers that gets us to sum(nums) / 2
        # if we are able to come up with a subset that equals sum(nums) / 2, then we know that the other partition 
        # must equal sums(nums) / 2
        
        # Outline:
        # check if sum(nums) is odd. If it is, return False immediately 
        # we set our target to be sum(nums) / 2
        # we maintain a 2D arr where:
            # the ith row indicates the partition sums we could make from the 0th elm to the ith elm in nums
            # the jth column indicates the subtarget sum
            # so dp[numIdx][subTarget] indicates whether a sum of subTarget can happen using 0th to numIdx elm
        
        # we iterate over the 2D arr:
            # for every idx in nums:
                # for every number from 0 to target inclusive:
                    # we check to see if arr[idx - 1][subTarget] = True
                        # if so we set the cell we're at arr[idx][subTarget] = True, and continue
                    # if we find that arr[idx - 1][subTarget - nums[idx]] == True
                        # set arr[idx][subTarget] == True
        # then we just return arr[len(nums) - 1][target]







        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        # make it (target + 1) length because a partition summing to 0 is possible
        # the partition summing to 0 is useful for when we want to consider a partition just including a single elm
        prev = [False] * (target + 1) # dp[subTarget]
        
        # the only sums possible with only the first elm is itself and 0
        prev[0] = True
        prev[0] = True


        for idx in range(1, len(nums)):
            elm = nums[idx]
            curr = [False] * (target + 1)
            for subTarget in range(target + 1):
                # check if it was already possible to make a partiton sum to subTarget
                # without this elm
                if prev[subTarget]:
                    curr[subTarget] = True
                # check to see if there is a possible partition that when given this elm,
                # will add up to subTarget
                elif prev[subTarget - elm]:
                    curr[subTarget] = True

            # end the computation early if we found that there is a partition possible
            if curr[subTarget]:
                return True
            # set up for next loop
            prev = curr
        # print(dp)
        return prev[target]














