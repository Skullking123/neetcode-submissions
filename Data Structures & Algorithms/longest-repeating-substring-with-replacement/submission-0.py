class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = {}
        res = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)

            maxf = max(maxf, counts[s[right]])
            while (right - left + 1) - maxf > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
            

        

        
            
        
        
        
        
            