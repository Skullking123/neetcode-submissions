class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        include = [0] * 26
        window = [0] * 26

        for letter in s1:
            index = ord(letter) - ord('a')
            include[index] += 1
        have = 0
        need = 26

        left = 0

        for right in range(len(s2)):
            letterIndex = ord(s2[right]) - ord('a')
            window[letterIndex] += 1

            if window[letterIndex] == include[letterIndex]:
                have += 1
            elif window[letterIndex] - 1 == include[letterIndex]:
                have -= 1

            if right < len(s1) - 1: # wait until our window becomes the same size as s1
                continue

            if include == window:
                return True
            
            # slide our window forward
            leftLetterIndex = ord(s2[left]) - ord('a')
            window[leftLetterIndex] -= 1
            if window[leftLetterIndex] == include[leftLetterIndex]:
                have += 1
            elif window[leftLetterIndex] + 1 == include[leftLetterIndex]:
                have -= 1

            left += 1
        
        return False

            
            
                

            
        


        