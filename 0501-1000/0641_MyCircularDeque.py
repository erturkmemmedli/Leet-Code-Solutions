class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.maxSize = k
        self.head = None
        self.tail = None
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.maxSize:
            node = ListNode(value)
            if self.head:
                node.next = self.head
                node.next.prev = node
                self.head = node
            else:
                self.head = node
                self.tail = node
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.maxSize:
            node = ListNode(value)
            if self.tail:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.tail = node
                self.head = node
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize        
        
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
