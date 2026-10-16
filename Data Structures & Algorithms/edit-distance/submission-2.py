class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Given two strings word1 and word2, return the minimum number
        # of operations to make word1 equal word2
        # The operations that can be done an unlimited number of times are:
            # Insert a char at any pos
            # Delete a char at any pos
            # Replace a char at any pos
        
        # First thought, layer-by-layer, bfs
        # From every word we traverse, we generate all the possible words we can make
        # by insertion, deletion, replacement and add them to the queue
        # This would be O(26^n) since we would be trying every permutation of letters
        # We would also be exploring words that we shouldn't be exploring either

        # monkeys
        # money
        # output 2
        # delete k and s

        # neatcdee
        # neetcode
        # output 3
        # replace a with e
        # insert o between c and d
        # delete an e at the end

        # base case
        if word1 == word2:
            return 0
        
        # (ptr1, ptr2) : min operations
        mem = {}

        def dfs(ptr1, ptr2, cSize):
            
            # we have ran out of letters for at least one of the words to process
            if ptr1 >= len(word1) or ptr2 >= len(word2):
                # if cSize > len(word2), we need to do cSize - len(word2) deletions
                # if len(word2) > cSize, we need to do len(word2) - cSize insertions
                # if they are equal, then no changes needed 
                return max(cSize, len(word2)) - min(cSize, len(word2))
            
            # no changes are needed 
            if word1[ptr1] == word2[ptr2]:
                return dfs(ptr1 + 1, ptr2 + 1, cSize)
            
            if (ptr1, ptr2) in mem:
                return mem[(ptr1, ptr2)]
            
            # we "insert" the letter we need to match
            insertion = dfs(ptr1, ptr2 + 1, cSize + 1)

            # we "delete" the letter
            deletion = dfs(ptr1 + 1, ptr2, cSize - 1)

            # we "replace" the letter:
            replacement = dfs(ptr1 + 1, ptr2 + 1, cSize)

            mem[(ptr1, ptr2)] = 1 + min(insertion, deletion, replacement)
            return mem[(ptr1, ptr2)]
        
        return dfs(0, 0, len(word1))

