class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums is a list of DISTINCT elms
        # list of all unique combinations of nums that sum to target
        # numbers can be repeated unlimited number of times
        # need a way to prune the tree to prevent duplicate combinations
        res = []
        def dfs(idx, pSum, curr):
            if pSum > target:
                return
            if idx == len(nums):
                return
            if pSum == target:
                res.append(curr.copy())
                return
            
            # traverse without the current elm
            dfs(idx + 1, pSum, curr)

            # add current elm
            pSum += nums[idx]
            dfs(idx, pSum, curr + [nums[idx]])

        dfs(0, 0, [])
        return res
