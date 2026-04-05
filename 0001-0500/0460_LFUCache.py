class ListNode:
    def __init__(self, key, value, next = None, prev = None, counter = 1):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
        self.counter = counter

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.next = None

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if node == self.head:
            if not node.next:
                self.head = None
                self.tail = None
            
            else:
                self.head = self.head.next
                self.head.prev = None

        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = {}
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.frequency[node.counter].remove(node)
        node.counter += 1

        if node.counter not in self.frequency:
            self.frequency[node.counter] = DoublyLinkedList()
                    
        self.frequency[node.counter].insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.frequency[node.counter].remove(node)
            node.value = value
            node.counter += 1

            if node.counter not in self.frequency:
                self.frequency[node.counter] = DoublyLinkedList()
                        
            self.frequency[node.counter].insert(node)

            return

        if not self.capacity:
            temp = 1
            
            while not self.frequency[temp].head:
                temp += 1
            
            head = self.frequency[temp].head
            self.frequency[temp].remove(head)
            del self.cache[head.key]

        node = ListNode(key, value)

        if node.counter not in self.frequency:
            self.frequency[node.counter] = DoublyLinkedList()
                    
        self.frequency[node.counter].insert(node)
        self.cache[key] = node

        if self.capacity:
            self.capacity -= 1     

# Alternative solution

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = self.head
            self.head.prev = None
            self.head.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        
    def remove(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        
class LFUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.frequency = defaultdict(DLinkedList)
        self.minfreq = 0
        
    def update(self, node: Node) -> None:
        freq = node.freq
        self.frequency[freq].remove(node)
        if freq == self.minfreq and self.frequency[freq].head is None:
            self.minfreq += 1
        node.freq += 1
        self.frequency[node.freq].insert(node)
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update(node)
        else:
            if self.size == self.capacity:
                dll = self.frequency[self.minfreq]
                node = dll.head
                dll.remove(node)
                del self.cache[node.key]
                self.size -= 1
            node = Node(key, value)
            self.cache[key] = node
            self.frequency[1].insert(node)
            self.minfreq = 1
            self.size += 1

    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
