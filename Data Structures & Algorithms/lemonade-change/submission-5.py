class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # A lemonade costs $5
        # Bills[i] is the amount the customer paid for a lemonade
        # Each customer will buy only one lemonade and pay with either $5, $10, or $20. 
        # You must provide the correct change to each customer at the time the customer paid
        # You do not have any change in hand at first

        # impossible if the first person pays with a anything > 5
        if bills[0] > 5:
            return False
        
        fives, tens = 0, 0        
        for bill in bills:
            
            # we don't need to give change
            if bill == 5:
                fives += 1
                continue
            elif bill == 10 and fives >= 1:
                tens += 1
                fives -= 1
            elif bill == 20 and (fives >= 1 and tens >= 1):
                fives -= 1
                tens -= 1
            elif bill == 20 and (fives >= 3):
                fives -= 3
            else:
                return False
        
        return True
                
            
            











