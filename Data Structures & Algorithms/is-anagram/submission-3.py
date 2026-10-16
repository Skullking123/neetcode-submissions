class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sCounts = {}
        tCounts = {}
        for letter in s:
            sCounts[letter] = sCounts.get(letter, 0) + 1
        
        for letter in t:
            tCounts[letter]= tCounts.get(letter, 0) + 1
        
        return sCounts == tCounts
        