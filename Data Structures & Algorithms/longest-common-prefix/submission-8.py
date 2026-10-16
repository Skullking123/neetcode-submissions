class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        shortestLen = float('inf')
        shortestStr = ""

        for string in strs:
            if len(string) < shortestLen:
                shortestLen = len(string)
                shortestStr = string
        
        for idx in range(shortestLen):
            for string in strs:
                if string[idx] != shortestStr[idx]:
                    return prefix
            prefix += shortestStr[idx]
        
        return prefix # if we get here, prefix is the shortest string
            