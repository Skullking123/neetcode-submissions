class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        combo = []

        def dfs(i):
            if i >= len(nums):
                res.append(combo.copy())
                return
            
            combo.append(nums[i])
            dfs(i + 1)

            combo.pop()
            dfs(i + 1)
        
        dfs(0)
        return res