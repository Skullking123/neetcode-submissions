class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if the min stack doesn't have elms or the val is less than the current min, append
        if not self.minimum or self.minimum[-1] >= val:
            self.minimum.append(val)

    def pop(self) -> None:
        # if the min stack has elements and the element we are popping is the minimum, pop it from the min stack
        if self.minimum and self.minimum[-1] == self.stack[-1]:
            self.minimum.pop()

        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
