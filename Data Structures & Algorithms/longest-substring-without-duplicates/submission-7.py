class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        alphabet = {}
        left = 0
        for right in range(len(s)):
            alphabet[s[right]] = alphabet.get(s[right], 0) + 1
            if alphabet[s[right]] > 1: # we have a repeated char in our window
                while alphabet[s[right]] > 1: # keep popping from the left until we remove the duplicated char
                    alphabet[s[left]] -= 1
                    left += 1
            print(s[right])
            print(left, right)
            res = max(res, right - left + 1)

        return res
