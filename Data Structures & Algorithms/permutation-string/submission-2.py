class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Counts = [0] * 26
        seen = [0] * 26
        
        right = 0

        if len(s1) > len(s2):
            return False

        s1 = s1.lower()
        s2 = s2.lower()

        for letter in s1:
            s1Counts[ord(letter) - 97] += 1

        while right < len(s2):
            print(s2[right])
            seen[ord(s2[right]) - 97] += 1

            if right > len(s1) - 1:
                seen[ord(s2[right - len(s1)]) - 97] -= 1
            
            if right >= len(s1) - 1:
                print(seen)
                if verifyLists(seen, s1Counts):
                    return True
                
            

            right += 1

        print(s1Counts)
        return False

    
def verifyLists(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False

    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
    
    return True

            
        


        