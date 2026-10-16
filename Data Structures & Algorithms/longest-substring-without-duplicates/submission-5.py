class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen = 0
        seen = set()

        sLen = len(s)
        while right < sLen:
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    # print(f"{s[left]} and {s[right]}")
                    left += 1 
            seen.add(s[right])
            maxLen = max(maxLen, len(seen))
            right += 1
            print(seen)

        return maxLen