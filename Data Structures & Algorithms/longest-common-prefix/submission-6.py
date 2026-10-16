class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        longest = ""
        for strg in strs:
            if len(strg) > len(longest):
                longest = strg
        
        for c in range(len(longest)):
            for strg in strs:
                if len(strg) <= c or strg[c] != longest[c]:
                    return res
            res += longest[c]

        return res
        
        