# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        

        prev = None
        curr = head

        while curr.next:

            prev = curr
            curr = curr.next

            new = ListNode(gcd(prev.val, curr.val)) 
            # insert the gcd in between prev and curr
            prev.next = new
            new.next = curr

        return head
            