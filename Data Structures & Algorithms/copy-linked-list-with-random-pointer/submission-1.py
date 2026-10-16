
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # need to return a deep copy of the list
        # each node has a random ptr that can point to a random node
            # that includes nodes that come after
            # will need a way to go back to nodes whose random ptrs point to a node that hasn't been created yet
            # nodes can have self-referential random ptrs
        # the values of each node need not be distinct
        
        # map each original to their copy
        nodes = {}
        nodes[None] = None
        rand_q = {}  # {randomPtr: [nodes whose rand ptr need to point to randomPtr]}

        dummy = Node(0)
        curr = head
        tail = dummy

        while curr:
            curr_copy = Node(curr.val)
            nodes[curr] = curr_copy
            print(curr.val)
            # assign rand ptr if we can
            if curr.random in nodes:
                curr_copy.random = nodes[curr.random]
            else:
                # save this node for later
                if curr.random not in rand_q:
                    rand_q[curr.random] = []
                rand_q[curr.random].append(curr_copy)
            
            # process any nodes whose rand ptrs are supposed to point to curr_copy
            while curr in rand_q and rand_q[curr]: 
                rand = rand_q[curr].pop()
                rand.random = curr_copy
            
            # append the copy
            tail.next = curr_copy
            tail = curr_copy

            # move ptr to next node
            curr = curr.next


        return dummy.next
        




