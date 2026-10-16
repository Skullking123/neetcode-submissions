class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        counts = {}
        longest = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            if counts[s[r]] > 1:
                while l < r and counts[s[r]] > 1:
                    counts[s[l]] -= 1
                    l += 1
            
            longest = max(longest, r - l + 1)

        return longest