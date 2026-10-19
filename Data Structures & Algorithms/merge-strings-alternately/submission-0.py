class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # given two strs, construct a new string by merging them in alternating order
        # if one str is longer than the other, append the remaining characters from the 
        # longer str to the result

                
        res = []

        ptr = 0

        while ptr < len(word1) or ptr < len(word2):
            if ptr < len(word1):
                res.append(word1[ptr])
            if ptr < len(word2):
                res.append(word2[ptr])
            ptr += 1
        
        return "".join(res)

        