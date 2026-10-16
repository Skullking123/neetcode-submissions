# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # most remove the nth node from the end of the list and return the beginning of the list
        # we could use a modified fast-slow ptr algorithm
        # have both fast and slow ptrs start at the head
            # give the fast ptr a headstart of n + 1 nodes
            # after the headstart, have both ptrs move one by one to the next node
        # essentially keeping our slow ptr always n + 1 nodes behind our fast ptr
        # once our fast ptr reaches the end of the list, our slow ptr should be pointing at the prev node of
        # the node we're trying to delete

        # will need to figure out the edge case when the node being deleted is the head

        # give fast the headstart
        fast = head
        for _ in range(n):
            fast = fast.next
        
        slow = head
        # the node behind the node we're trying to del
        prev = None
        # have both ptrs keep pace until fast reaches the end
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev:
            # delete the node
            prev.next = prev.next.next
        else:
            # we're deleting the head
            head = head.next

        return head