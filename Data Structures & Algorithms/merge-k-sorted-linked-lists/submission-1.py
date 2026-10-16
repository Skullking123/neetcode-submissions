# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # given an arr of linked lists sorted in ascending order
        # return the sorted linked list by merging all of the lists together

        # Create a sorted list by taking the smallest element from the front of each list
        # and adding it to our result

        res = ListNode(0)
        tail = res
        while True:
            minimum, m_idx = float('inf'), -1
            for idx in range(len(lists)):
                if lists[idx] == None:
                    continue
                if lists[idx].val < minimum:
                    minimum, m_idx = lists[idx].val, idx
            
            if m_idx == -1:
                break

            next_elm = lists[m_idx]
            # move the ptr in the list along
            lists[m_idx] = lists[m_idx].next

            # append our next elm
            next_elm.next = None
            tail.next = next_elm
            tail = next_elm

        return res.next
