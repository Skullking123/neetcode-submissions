class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:  
        # nums can have duplicates
        # each indiv elm can only be used at most once
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














        # return a list of all unique combinations of candidates that sum to target
        # each candidate can only be chosen once
        # each subset is a possible sum 
        # process each subset

        # duplicate elements could cause combinations to repeat
        candidates.sort()
        res = []
        currSum = 0
        currCand = []
        def dfs(idx):
            nonlocal currSum
            print(currCand)
            # no more elms
            if idx == len(candidates):
                if currSum == target:
                    res.append(currCand.copy())
                # go back
                return
            # go back
            if currSum > target:
                return

            
            # the elm is present
            currSum += candidates[idx]
            currCand.append(candidates[idx])
            dfs(idx + 1)
            # the elm is not present
            currSum -= candidates[idx]
            currCand.pop()
            dfs(idx + 1)

            
        dfs(0)
        return res



        
