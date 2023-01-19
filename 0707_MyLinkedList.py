class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            node = ListNode(val)
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.tail = ListNode(val)
            self.head = self.tail
        else:
            node = ListNode(val)
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif 0 < index < self.length:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            saved = temp.next
            node = ListNode(val)
            temp.next = node
            node.next = saved
            self.length += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index < self.length:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            if index == self.length - 1:
                self.tail = temp
            self.length -= 1

    def printLinkedList(self):
        temp = self.head
        linkedList = str(temp.val)
        while temp:
            temp = temp.next
            if temp:
                linkedList += ", " + str(temp.val)
        print(linkedList)
        print(self.length)
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
