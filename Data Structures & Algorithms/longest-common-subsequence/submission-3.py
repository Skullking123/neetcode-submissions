class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Given two strings text1 and text2, return the length of the longest common subeq
        # between the two strings if one exists, otherwise return 0
        # A subseq is a seq that can be derived from the given seq by deleting some or no elms without changing 
        # the relative order of the remaining characters

        # For any given char in text1, it is either included or excluded in the subseq 
            # If we decide to include a char, we try to find a matching letter in text2 and then dfs down it
            # attempting to use the char from text1 and text2 to come up with a new subseq
            # If we decide to exclude it, we ignore it and look towards the next letter

        # A longer subseq can be made by appending a common letter to a common subseq alr made by letters
        # either that were in front or behind
        # subseq may be reused for other common subseq, this could lead to repeated computations
        
        # maintain a res = 0 that will keep track of the length of the longest subseq we find
        # For every char, char1, in text1:
            # We go through text2 trying to find matching chars to char1
                # If we find a matching char, we drill down
        # Then we move on to the next char in text1, exlcuding char1

        # (t1_idx, t2_idx): length
        subseqLen = {}
        self.res = 0
        def subseq(idx1, idx2):
            # don't reprocess this common subseq again

            if (idx1, idx2) in subseqLen:
                return subseqLen[(idx1, idx2)]
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            print(idx1, idx2)
            
            c1 = text1[idx1]
            subLen = 0
            # see if there is a matching char
            for t2 in range(idx2, len(text2)):
                c2 = text2[t2]
                if c1 == c2:
                    # try to extend this subseq using the letters to the right
                    subLen = max(subLen, 1 + subseq(idx1 + 1, t2 + 1))
            
            self.res = max(self.res, subLen)

            # make a subseq exlcuding the elm
            subLen = max(subLen, subseq(idx1 + 1, idx2))
            subseqLen[(idx1, idx2)] = subLen
            return subLen

        subseq(0, 0)
        return self.res