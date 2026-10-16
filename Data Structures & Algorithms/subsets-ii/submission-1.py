class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # every elm in the list has two possibilities:
            # they're present
            # they're absent
        # we must be able to backtrack to build additional sets out of an alr existing set
        # we can't repeat subsets
        
        nums.sort()
        res = []
        curr = []
        def dfs(idx):
            # no more elms
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            # include elm @ idx
            curr.append(nums[idx])
            dfs(idx + 1)
            
            # don't include elm @ idx
            curr.pop()
            # skip over duplicates of elm @ idx
            jdx = idx + 1
            while jdx < len(nums) and nums[jdx] == nums[idx]:
                jdx += 1
            dfs(jdx)
        
        dfs(0)
        return res



        nums = sorted(candidates)
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
            dfs(idx + 1)

            # traverse without the current elm
            curr.pop()
            for elm in range(idx + 1, len(nums)):
                if nums[elm] != nums[elm - 1]:
                    dfs(elm)
                    break
                    

        dfs(0)
        return res