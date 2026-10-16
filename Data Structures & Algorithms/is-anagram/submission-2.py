class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in s_letters:
                s_letters[letter] = s_letters[letter] + 1
            else:
                s_letters[letter] = 1

        for letter in t:
            if letter in t_letters:
                t_letters[letter] = t_letters[letter] + 1
            else:
                t_letters[letter] = 1


        if s_letters.items() != t_letters.items():
            return False

        return True
        

            
        
        