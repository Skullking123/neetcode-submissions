class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # given an input string s, and a pattern p
        # return true if the pattern matches the entire input string, otherwise return false
        # . matches any single character
        # * matches zero or mor of the preceding element

        # Any letter in p must match to the same letter in s
        # Any . in p can match to any letter in s
        # Any * in p can match to however long a sequence of the previous letter in p in s
        mem = {}

        regex = []
        for idx in range(len(p)):
            if p[idx] == "*":
                continue
            if idx + 1 < len(p) and p[idx + 1] == "*":
                regex.append(f"{p[idx]}*")
            else:
                regex.append(p[idx])
        
        # print(regex)
        # mississippi
        # 012345678
        def dfs(sPtr, rPtr):
            # print(sPtr, rPtr)
            if sPtr >= len(s) and rPtr >= len(regex):
                return True
            elif sPtr >= len(s):
                for idx in range(rPtr, len(regex)):
                    if regex[idx][-1] != "*":
                        return False
                return True
            elif rPtr >= len(regex):
                return False
            
            if (sPtr, rPtr) in mem:
                return mem[(sPtr, rPtr)]

            res = False
            if regex[rPtr][-1] == "*":
                # extend the *
                if regex[rPtr][0] == "." or regex[rPtr][0] == s[sPtr]:
                    res = res or dfs(sPtr + 1, rPtr)
                # match with nothing
                res = res or dfs(sPtr, rPtr + 1)
            else:
                if regex[rPtr] == "." or regex[rPtr] == s[sPtr]:
                    res = res or dfs(sPtr + 1, rPtr + 1)
            
            mem[(sPtr, rPtr)] = res
            return mem[(sPtr, rPtr)]
            

        return dfs(0, 0)