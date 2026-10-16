class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedStr = ""
        reversedStr = ""

        for letter in s:
            if letter.isalnum():
                sanitizedStr = sanitizedStr + letter.lower()
                reversedStr = letter.lower() + reversedStr
        
        return sanitizedStr == reversedStr
