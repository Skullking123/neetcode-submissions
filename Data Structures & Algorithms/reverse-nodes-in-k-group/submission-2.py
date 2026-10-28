# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Given a singly linked list head, and a positive int k
        # Reverse every consecutive group of k nodes
        # If there are fewer than k nodes, return the list as is
        # Return the modified list after reversing 
        # Only allowed to modify the nodes' next pointers, not the values of the nodes
        
        
        # have two pointers: res and curr
        # res is a pointer to the final list that we are going to return
        # curr is the current subgroup that we are reversing
        # maintain two pointers that start at head: fast and slow
        # for each iteration until fast reaches the end
            # the fast pointer moves exactly k steps
            # the slow pointers move 1 step at a time, appending each node to the front of curr
                # moves until has caught up with fast
            # append curr to the end of res
        # return res

        # start with a dummy node to ignore the
        # case of appending to an empty list
        res = ListNode(-1)
        rtail = res
        fast = head
        slow = head

        while fast:
            curr = None
            # move fast k steps ahead or as however many steps to the end
            # whichever is less
            lgth = 0
            for _ in range(k):
                # we've reached the end
                if not fast:
                    break
                fast = fast.next
                lgth += 1
            
            # we don't have enough nodes, leave them be and exit 
            if lgth < k:
                rtail.next = slow
                break

            # print(f"fast: {fast.val if fast else fast}")
            # the first node of the group is always the tail
            ctail = slow
            # print(f"ctail: {ctail.val}")
            # move slow up until slow has caught up with fast
            while slow != fast:
                # append node that slow is pointing at to the front of curr
                temp = slow.next
                slow.next = curr
                curr = slow
                slow = temp
            
            ptr = curr
            # while ptr:
            #     print(ptr.val)
            #     ptr = ptr.next
            # print()

            # append curr to the tailend of res
            rtail.next = curr
            rtail = ctail
        
        return res.next








