class MyQueue:
    # implement a queue using only two stacks
    # can only use push to top, peek/pop from top, size, and is empty

    def __init__(self):
        self.actual = []
        self.holding = []
    
    # pushes an elm to the back of the queue
    def push(self, x: int) -> None:
        # pop all the elms from the actual stack
        # into the holding stack to invert it
        for _ in range(len(self.actual)):
            elm = self.actual.pop()
            self.holding.append(elm)
        # now append the elm
        self.holding.append(x)
        # now pop everything from holding and
        # push it into the actual stack to have
        # the elms back in reverse order
        for _ in range(len(self.holding)):
            elm = self.holding.pop()
            self.actual.append(elm)
            
        
    # Removes and returns the first element in the queue
    def pop(self) -> int:
        return self.actual.pop()
    # Returns the first elm in the queue
    def peek(self) -> int: 
        return self.actual[-1]
    # Returns true if the queue is empty, false otherwise
    def empty(self) -> bool:
        return len(self.actual) == 0
    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()