class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteFromCache(node)
            self.insertAfterHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.deleteFromCache(node)
            self.insertAfterHead(node)
        else:
            if len(self.cache) == self.capacity:
                self.deleteBeforeTail()
            node = ListNode(key, value)
            self.cache[key] = node
            self.insertAfterHead(node)
    
    def deleteFromCache(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertAfterHead(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def deleteBeforeTail(self):
        if len(self.cache) == 0:
            return
        tail = self.tail.prev
        del self.cache[tail.key]
        self.deleteFromCache(tail)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
