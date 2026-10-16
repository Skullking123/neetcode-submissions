class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # given two ints n and k, return all possible combinations of k
        # numbers chosen from the range [1, n]
        # You may return teh answer in any order

        # for any given n, we can say we can either:
            # use n and then make combinations of size k - 1 out of [1, n - 1]
            # not use n and make combinations of size k out of [1, n - 1]

        # only one way we can make a combination of 0 elements
        res = []
        curr = []
        def dfs(num):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if num > n:
                return 

            # exclude
            dfs(num + 1)
            # include 
            curr.append(num)
            dfs(num + 1)
            curr.pop()
        
        dfs(1)

        return res
