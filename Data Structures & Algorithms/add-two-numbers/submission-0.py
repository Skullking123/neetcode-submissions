# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        res = None
        tail = None


        curr1 = l1
        curr2 = l2
        decimal = 0
        remainder = 0
        while curr1 or curr2:
            val1 = 0
            if curr1:
                val1 = curr1.val
                curr1 = curr1.next
            
            val2 = 0
            if curr2:
                val2 = curr2.val
                curr2 = curr2.next
            
            digitSum = val1 + val2 + remainder 
            if digitSum > 9:
                digitSum = digitSum - 10
                remainder = 1
            else:
                remainder = 0
            
            if not res:
                res = ListNode(digitSum)
                tail = res
            else:
                tail.next = ListNode(digitSum)
                tail = tail.next
        
        if remainder != 0:
            tail.next = ListNode(remainder)

        return res



        
        