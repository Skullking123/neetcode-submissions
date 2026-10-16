class Solution:
    def checkValidString(self, s: str) -> bool:
        # given a string s, s contains only ( ) and *
        # return true if s is valid
        # * can be ( ) or ""
        
        # (*****)
        # (*****(
        # )*****)
        # )*****(

        left = []
        stars = []
        # iterate through the string maintaining our stacks
        for idx in range(len(s)):
            c = s[idx]
            if c == "(":
                left.append(idx)
            elif c == "*":
                stars.append(idx)
            else:
                # we prioritize consuming the left parens so that we can save the stars for maximum flexibility later
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        # there may still be some left parens left because there may be some 
        # left parens that need a star to complete them
        while left:
            if stars and stars[-1] > left[-1]:
                stars.pop()
                left.pop()
            else:
                return False
        
        return True


        # s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        # false
        #"(((((*(((((*((**(((*)*((((**))*)*)))))))()()))((*(((((*()*(**)()"