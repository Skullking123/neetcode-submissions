class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # list of all unique combinations of nums that sum to target
        # numbers can be repeated unlimited number of times
        # need a way to prune the tree to prevent duplicate combinations
        
        res = []
        currSum = 0
        currCombo = []

        def dfs(idx):
            nonlocal currSum
            currSum += nums[idx]
            currCombo.append(nums[idx])
            # print(currCombo)
            # don't go further
            if currSum > target:
                currSum -= nums[idx]
                currCombo.pop()
                return
            # add to res, and go back
            elif currSum == target:
                res.append(currCombo.copy())
                currSum -= nums[idx]
                currCombo.pop()
                return
            
            # traverse 
            for elmIdx in range(idx, len(nums)):
                dfs(elmIdx)
            
            # go back
            currSum -= nums[idx]
            currCombo.pop()

        for elmIdx in range(len(nums)):
            dfs(elmIdx)
        return res