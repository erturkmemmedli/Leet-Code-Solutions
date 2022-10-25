class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.head = None
        self.tail = None
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.length:
            return False
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.tail.next = self.head   
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        if self.tail:
            self.tail.next = self.head
        self.length -= 1
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
