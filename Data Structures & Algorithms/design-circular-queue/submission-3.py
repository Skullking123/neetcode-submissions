class MyCircularQueue:

    def __init__(self, k: int):
        self.start = 0
        self.end = 0
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            # print("Enqueue full", self.queue, self.start, self.end)
            return False
        self.queue[self.end] = value
        self.end += 1
        if self.end == len(self.queue):
            self.end = 0
        # print("Enqueue", self.queue, self.start, self.end)
        return True

    def deQueue(self) -> bool:
        # check if there is an element
        if self.isEmpty():
            # print("Dequeue empty", self.queue, self.start, self.end)
            return False
        
        self.queue[self.start] = None
        self.start += 1
        if self.start == len(self.queue):
            self.start = 0
        # print("Dequeue", self.queue, self.start, self.end)
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            # print("Front empty", self.queue, self.start, self.end)
            return -1
        # print("Front", self.queue, self.start, self.end)
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        # print("Rear", self.queue, self.start, self.end)
        last = self.queue[self.end - 1] if self.end != 0 else self.queue[-1]
        return last

    def isEmpty(self) -> bool:
        return self.queue[self.start] == None

    def isFull(self) -> bool:
        return self.queue[self.end] != None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()