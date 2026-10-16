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
        else:
            # remove the key from where it is
            self.nodes[key].prev.next = self.nodes[key].next
            self.nodes[key].next.prev = self.nodes[key].prev
        
        # insert the node at the head of the list
        self.nodes[key].prev = self.head
        self.nodes[key].next = self.head.next
        self.nodes[key].next.prev = self.nodes[key]
        self.head.next = self.nodes[key]

        return self.nodes[key].value


    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            # make a new node
            self.nodes[key] = Node(key, value)
        else: 
            # remove the key from where it is
            self.nodes[key].prev.next = self.nodes[key].next
            self.nodes[key].next.prev = self.nodes[key].prev
            self.nodes[key].value = value
        
        # insert the node at the head of the list
        self.nodes[key].prev = self.head
        self.nodes[key].next = self.head.next
        self.nodes[key].next.prev = self.nodes[key]
        self.head.next = self.nodes[key]
        
        if len(self.nodes) > self.capacity:
            # remove the least recently used node
            to_remove = self.tail.prev.key
            self.tail.prev = self.nodes[to_remove].prev
            self.nodes[to_remove].prev.next = self.tail
            del self.nodes[to_remove]

            
