# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        end = None

        head1 = list1
        head2 = list2

        while head1 or head2:
            selected = None
            if not head1:
                selected = head2
                head2 = head2.next
            elif not head2:
                selected = head1
                head1 = head1.next
            elif head1.val <= head2.val:
                selected = head1
                head1 = head1.next
            else:
                selected = head2
                head2 = head2.next
            
            if res is None:
                res = selected
                res.next = None
                end = res
            else:
                end.next = selected
                end = selected
                end.next = None
            
        return res