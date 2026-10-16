class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return a list of all permutations
        # nums is a list of UNIQUE ints
        # the return does not need to follow a certain order

        # dfs down
        # at each node we decide what to add next
            # we will need to keep track of what has been used
            # only go down paths where we have used an elm
        # when we run out of elms, we found a permutation - append it to res
        
  
        res = []

        def dfs(curr):

            if len(curr) == len(nums):
                res.append(curr)
                return

            # decide where to go next
            for elm in range(len(nums)):
                if nums[elm] not in curr:
                    dfs(curr + [nums[elm]])

        dfs([])
        return res











        res = []
        used = set()

        def dfs(curr):

            if len(curr) == len(nums):
                res.append(curr)
                return

            # decide where to go next
            for elm in range(len(nums)):
                if nums[elm] not in used:
                    used.add(nums[elm])
                    dfs(curr + [nums[elm]])
                    used.remove(nums[elm])

        dfs([])
        return res









        curr = []
        res = []
        used = set()

        def dfs(idx):

            if len(used) == len(nums):
                res.append(curr.copy())
                return
            
            # add curr
            curr.append(nums[idx])
            used.add(nums[idx])

            # decide where to go next
            for elm in range(len(nums)):
                if nums[elm] not in used:
                    dfs(elm)
            
            # go back
            curr.pop()
            used.remove(nums[idx])

        dfs(0)
        return res