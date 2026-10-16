# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # given two linked lists that represent a non-negative integer, add them
        # digits are stored in reverse order (convienent)
        # will need to deal with carrying over 
        # will need to deal with numbers of differing lengths (100000 + 10)

        curr1 = l1
        curr2 = l2

        # we can build our res backwards since we are starting from the ones place
        dummy = ListNode(0)
        tail = dummy
        carryOver = False
        while curr1 or curr2:
            # in case we run out of digits of either one
            d1 = curr1.val if curr1 else 0
            d2 = curr2.val if curr2 else 0            

            # sum the digits
            digit_sum = d1 + d2
            
            # check if we need to carry over for the this set of digits
            if carryOver:
                digit_sum += 1
                carryOver = False
            
            # check to see if we need to carry over for the next set
            if digit_sum > 9:
                digit_sum -= 10
                carryOver = True
            
            # append to our res
            res_node = ListNode(digit_sum)
            tail.next = res_node
            tail = res_node

            # move our pointers
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        if carryOver:
            tail.next = ListNode(1)

        return dummy.next
            

