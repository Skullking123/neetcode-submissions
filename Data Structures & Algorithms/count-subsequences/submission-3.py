class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # given two strings s and t, return the number of distinct subsequences of s which are equal to t

        # first thought
        # iterate through every letter of s:
        # we can either include a letter or exclude it:
            # if the letter helps us build t:
                # we can make a subsequence that includes this
                # we can exclude this letter and attempt to look for another instance of the letter
            # if the letter doesn't help us build t:
                # we exclude it, and traverse further down t looking for a letter that helps us build our letter
        
        mem = {}
        
        def dfs(sPtr, tPtr):
            # we completed a subsequence
            if tPtr == len(t):
                return 1
            # we are not able to complete a subsequence
            if sPtr == len(s):
                return 0
            
            if (sPtr, tPtr) in mem:
                return mem[(sPtr, tPtr)]

            p_seq = dfs(sPtr + 1, tPtr + 1) + dfs(sPtr + 1, tPtr) if s[sPtr] == t[tPtr] else dfs(sPtr + 1, tPtr)
            mem[(sPtr, tPtr)] = p_seq
            return p_seq

        return dfs(0, 0)