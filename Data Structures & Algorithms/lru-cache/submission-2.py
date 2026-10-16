class Node:
    def __init__(self, key: int, value: int, prev: Node = None, next: Node = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    
    # initialize the LLRU cache of size capacity
    # get returns the value for "key" if it exists. Returns -1 otherwise
    # put updates the key-value pair if it axists. Otherwise it will add the key-value pair
    # and evict the least recently used key if capacity is exceeded

    # get and put must each run in O(1) time complexity
    
    # First thoughts go to using a hash set to store key-value pairs to access in O(1)
        # would need a way to keep track of whats been recently used (use a sort of queue?)
        # the problem with a queue is that accessing values in the queue is O(n)
    
    # What if we use a hash set where the key-value pairs are {key: Node that contains value}, the nodes
    # would be stored as a linked a list. Then if we want to know what is the least recently used, we just look at the tail
    # and pop from the tail. When we get/put a key, we can use the hashset to go straight to the node, to remove it where it is
    # in the linked list, and move it to the front. In order to remove a node potentially in the middle, would need access to the prev
    # node, so probably use a doubly linked list
    

    def __init__(self, capacity: int):
        self.head = Node(-1, -1) # use a dummy node
        self.tail = Node(-1, -1) # use a dummy node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        # get the nodes whose ptrs need adjusting
        curr = self.nodes[key]
        next = curr.next
        prev = curr.prev

        # make the next and prev node point to each other
        next.prev = prev
        prev.next = next

        # get the first node of the list
        first = self.head.next

        # make curr and first pt to each other
        curr.next = first
        first.prev = curr

        # attach head to curr
        self.head.next = curr
        curr.prev = self.head

        return curr.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            # move the key to the front of the list
            self.get(key) 
            # update the value
            self.head.next.value = value
            return 

        # add the new key-value to the cache
        new = Node(key, value)
        self.nodes[key] = new
        # get the first node
        first = self.head.next
        
        # make the new node and first pt to each other
        new.next = first
        first.prev = new

        # make head and new point to each other
        self.head.next = new
        new.prev = self.head

        # exceeded capacity, need to remove a node from the end
        if len(self.nodes) > self.capacity:

            # get the nodes that need adjusting
            old = self.tail.prev
            sec_oldest = old.prev

            # make tail and sec_oldest point to each other
            sec_oldest.next = self.tail
            self.tail.prev = sec_oldest
            
            # delete the node from lookup
            del self.nodes[old.key]
            
