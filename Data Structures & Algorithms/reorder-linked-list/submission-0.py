# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the list such that the order goes as follows:
        # [0, n-1, 1, n-2, 2, n-3, ...]
        # notice the list is like pair-wise merging:
            # [0, 1, 2, 3...]
            # [n-1, n-2, n-3, n-4, ...]
        # idea: split the list in half, and reverse the 2nd half. Then merge
        slow = head
        fast = head
        
        # get slow to the midpoint of list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_half = slow.next
        # split the list into two halfs
        first_half = head
        slow.next = None

        # reverse 2nd half
        prev = None
        sec_half_head = None
        while sec_half:
            holder = sec_half.next
            sec_half.next = prev
            prev = sec_half
            sec_half = holder
        # sec_half point to the new head
        sec_half = prev

        # merge the two halfs
        while first_half or sec_half:
            first_holder = first_half.next
            first_half.next = sec_half
            if sec_half:
                sec_holder = sec_half.next
                sec_half.next = first_holder
                sec_half = sec_holder
            first_half = first_holder
        
                
            

        
            