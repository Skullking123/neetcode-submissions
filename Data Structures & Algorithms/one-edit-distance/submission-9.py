class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        tPtr = 0
        sPtr = 0
        diffs = 0
        changeFound = False
        while tPtr < len(t) and sPtr < len(s):
            if t[tPtr] == s[sPtr]:
                print("No change")
                tPtr += 1
                sPtr += 1
            elif tPtr < len(t) - 1 and sPtr < len(s) - 1 and t[tPtr + 1] == s[sPtr + 1] and len(s) == len(t): # replacement
                print("replacement")
                if changeFound:
                    return False
                tPtr = tPtr + 1
                sPtr = sPtr + 1
                tPtr += 1
                sPtr += 1
                changeFound = True
            elif tPtr < len(t) - 1 and t[tPtr + 1] == s[sPtr]: # insertion
                print("insertion")
                if changeFound:
                    return False
                tPtr = tPtr + 1
                tPtr += 1
                sPtr += 1
                changeFound = True
            elif sPtr < len(s) - 1 and t[tPtr] == s[sPtr + 1]: # deletion
                print("deletion")
                if changeFound:
                    return False
                sPtr = sPtr + 1
                tPtr += 1
                sPtr += 1
                changeFound = True
            else:
                print("diff letters")
                if changeFound:
                    return False
                changeFound = True
                tPtr += 1
                sPtr += 1
            
            
        
        sReachEnd = (sPtr == len(s))
        tReachEnd = (tPtr == len(t))
        print(changeFound)
        print(sReachEnd)
        print(tReachEnd)
        if changeFound and sReachEnd and tReachEnd:
            return True
        elif not changeFound and sReachEnd and tReachEnd:
            return False
        elif changeFound and (not sReachEnd or not tReachEnd):
            return False
        else:
            return True
