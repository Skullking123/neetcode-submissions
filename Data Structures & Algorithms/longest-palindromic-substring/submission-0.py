class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return the longest substring of s that is a palindrome
        # a palindrome is a string that reads thes ame forward and backward

        # a palindrome can be made from two consecutive palindromes if they are equal

        # an even length palindrome has two center chars that are the same
        # an odd length palindrome has one center char 
        
        centers = []
        for idx in range(len(s)):
            if centers and s[centers[-1][1]] == s[idx]:
                centers.append([centers[-1][1], idx])
            centers.append([idx, idx])
        
        res_len = 0
        res = ""
        for cl, cr in centers:
            curr = "" + s[cl] + s[cr] if cl != cr else "" + s[cl]
            curr_len = len(curr)
            cl -= 1
            cr += 1
            while cl >= 0 and cr <= len(s) - 1 and s[cl] == s[cr]:
                curr = s[cl] + curr + s[cr]
                curr_len += 2
                cl -= 1
                cr += 1
            if curr_len > res_len:
                res_len = curr_len
                res = curr
            

        return res