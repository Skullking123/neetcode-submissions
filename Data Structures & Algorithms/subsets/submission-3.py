class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # every elm in the list has two possibilities:
            # they're present
            # they're absent
        
        # we must be able to backtrack to build additional sets out of an alr existing set
        res = []
        curr = []
        def dfs(idx):
            # no more elms
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            # they're present
            curr.append(nums[idx])
            dfs(idx + 1)
            # they're absent
            curr.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res