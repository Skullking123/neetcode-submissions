class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums is a list of DISTINCT elms
        # list of all unique combinations of nums that sum to target
        # numbers can be repeated unlimited number of times
        # need a way to prune the tree to prevent duplicate combinations
        res = []
        curr = []
        def dfs(idx):
            pSum = sum(curr)
            if pSum >= target or idx == len(nums):
                if pSum == target:
                    res.append(curr.copy())
                return

            

            # add current elm
            curr.append(nums[idx])
            dfs(idx)

            # traverse without the current elm
            curr.pop()
            dfs(idx + 1)

        dfs(0)
        return res
