class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Find the subarr with the largest sum and return the sum
        # Implement kadanes

        # Kadanes attempts to find the maximum sum of all possible subarrs that 
        # end at exactly index i

        # The idea is at each index i:
            # Can we achieve a bigger sum by attaching nums[i] to the maximum sum
            # of all possible subarrs that end at i - 1
            # If yes, then include it
            # Otherwise we leave nums[i] as a stand alone subarr
        
        prev = float('-inf')
        res = nums[0]
        for idx in range(len(nums)):
            curr = max(nums[idx], nums[idx] + prev)
            res = max(res, curr)
            prev = curr
        # print(sums)
        return res
