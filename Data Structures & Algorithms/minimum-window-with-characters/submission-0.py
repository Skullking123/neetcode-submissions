class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        tCounts = {}
        window = {}
        left = 0 # ptr to the left side of our window 

        # initialize our counts
        for c in range(len(t)):
            tCounts[t[c]] = tCounts.get(t[c], 0) + 1

        have = 0
        need = len(tCounts)
        res = (0, 0)
        resLen = float('infinity')
        for right in range(len(s)):
            
            window[s[right]] = window.get(s[right], 0) + 1
            if window[s[right]] == tCounts.get(s[right], 0):
                have += 1

            while have == need:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = (left, right)
                window[s[left]] -= 1
                if window[s[left]] < tCounts.get(s[left], 0):
                    have -= 1
                left += 1

        if resLen == float('infinity'):
            return ""
        else:
            return s[res[0]:(res[1] + 1)]
            
    


        

        
        
        

        
            


