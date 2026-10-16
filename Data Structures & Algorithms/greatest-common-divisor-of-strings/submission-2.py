class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Return the largest string x such that x divides both str1 and str2
        # For two strings s and t, t divides s if and only if s = t + t + ... + t
        # n = len(str1)
        # m = len(str2)
        # brute force O(m * n)
        # we start by trying to divide str1 with the entirety of s2
        # if that doesn't work, try to divide str1 with the entirety of s2 without the last char in s2
        # if that doesn't work, try to divide str1 with the s2 without the last 2 chars
        # ... repeat until we either find one that works, or run out of str2
        # if we reach this point, then nothing works and return ""

        if len(str1) < len(str2):
            str1, str2 = str2, str1


        for subStrLen in range(len(str2), 0, -1):

            if len(str1) % subStrLen != 0 or len(str2) % subStrLen:
                continue

            t = str2[:subStrLen]
            
            
            match = True
            for idx in range(len(str1)):
                if str1[idx] != t[idx % subStrLen]:
                    match = False
                    break
            
            if not match:
                continue
            
            for idx in range(len(str2)):
                if str2[idx] != t[idx % subStrLen]:
                    match = False
                    break
            
            if match:
                return t

            
        return ""