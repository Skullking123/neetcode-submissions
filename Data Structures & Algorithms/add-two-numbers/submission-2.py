# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        # 1
        #   9
        # + 5
        # 1 4

        res = None
        resTail = None
        remainder = 0

        while curr1 or curr2:
            digit1 = 0
            digit2 = 0

            if curr1:
                digit1 = curr1.val
                curr1 = curr1.next
            if curr2:
                digit2 = curr2.val
                curr2 = curr2.next
            
            sum = digit1 + digit2 + remainder
            
            if sum > 9:
                sum = sum % 10
                remainder = 1
            else:
                remainder = 0
            
            if not res:
                res = ListNode(sum)
                resTail = res
            else:
                newTail = ListNode(sum)
                resTail.next = newTail
                resTail = newTail
        
        if remainder != 0:
            resTail.next = ListNode(remainder)
        
        return res





        
        