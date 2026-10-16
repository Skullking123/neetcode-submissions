class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxEnding = float('-inf')
        res = float('-inf')

        # implement kadanes alg
        for num in nums:
            maxEnding = max(num, maxEnding + num)
            res = max(res, maxEnding)
        
        return res