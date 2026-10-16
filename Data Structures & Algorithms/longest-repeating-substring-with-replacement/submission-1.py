class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0 
        
        counts = {}
        mostFreq = 0
        maxLen = 0
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1

            mostFreq = max(mostFreq, counts[s[right]])

            while right - left + 1 - mostFreq > k:
                counts[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen
            





        
        