class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        sLetters = dict()
        tLetters = dict()
        if (len(s) == len(t)):
            for letter in range(0, len(s)):
                if s[letter] in sLetters:
                    sLetters[s[letter]] = sLetters[s[letter]] + 1
                else:
                    sLetters[s[letter]] = 1
                
                if t[letter] in tLetters:
                    tLetters[t[letter]] = tLetters[t[letter]] + 1
                else:
                    tLetters[t[letter]] = 1
                    
            if sLetters == tLetters:
                res = True

        return res
            
        
        