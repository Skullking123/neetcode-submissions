class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # return a list of all possible lists of palindromic substrings that can be made from s
        # list may be in any order

        partitions = set()
        seen = set()
        def dfs(subStrs: List[str]):
            
            # go through the list and see if there are any other palindromes to make
            # if so, drill down each of them
            for idx in range(len(subStrs)):
                # if two consecutive subStrs form a palindrome
                partitions.add(tuple(subStrs))
                if idx + 1 < len(subStrs) and subStrs[idx] == subStrs[idx + 1][::-1]:
                    next = subStrs[:idx] + [subStrs[idx] + subStrs[idx + 1]] + subStrs[idx + 2:]
                    if tuple(next) not in seen:
                        seen.add(tuple(next))
                        dfs(subStrs[:idx] + [subStrs[idx] + subStrs[idx + 1]] + subStrs[idx + 2:])
                
                # if a subtr is sandwiched between two strs that would form a palindrome 
                if idx - 1 >= 0 and idx + 1 < len(subStrs) and subStrs[idx - 1] == subStrs[idx + 1][::-1]:
                    next = subStrs[:idx - 1] + [subStrs[idx -1 ] + subStrs[idx] + subStrs[idx + 1]] + subStrs[idx + 3:]
                    if tuple(next) not in seen:
                        seen.add(tuple(next))
                        dfs(subStrs[:idx - 1] + [subStrs[idx -1 ] + subStrs[idx] + subStrs[idx + 1]] + subStrs[idx + 2:])
            

        start = list(s)
        dfs(start)
        res = []
        for partition in partitions:
            res.append(list(partition))
        
        return res
