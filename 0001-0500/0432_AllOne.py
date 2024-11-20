class Node:
    def __init__(self, freq: int):
        self.prev = None
        self.next = None
        self.freq = freq
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)
            if not node.next:
                new_node = Node(freq + 1)
                node.next = new_node
                new_node.prev = node
                new_node.keys.add(key)
                self.map[key] = new_node
                self.tail = new_node
            else:
                next = node.next
                if next.freq - freq > 1:
                    new_node = Node(freq + 1)
                    node.next = new_node
                    new_node.prev = node
                    new_node.next = next
                    next.prev = new_node
                    new_node.keys.add(key)
                    self.map[key] = new_node
                else:
                    next.keys.add(key)
                    self.map[key] = next
            if not node.keys:
                self.removeNode(node)
        else:
            if not self.head:
                node = Node(1)
                self.head = node
                self.tail = node
                node.keys.add(key)
                self.map[key] = node
            elif self.head.freq != 1:
                node = Node(1)
                node.next = self.head
                self.head.prev = node
                self.head = node
                node.keys.add(key)
                self.map[key] = node
            else:
                self.map[key] = self.head
                self.head.keys.add(key)

    def dec(self, key: str) -> None:
        if key not in self.map:
            raise Exception(f"{key} doesn't exist in map.")
        node = self.map[key]
        freq = node.freq
        node.keys.remove(key)
        if freq == 1:
            del self.map[key]
        elif node.prev:
            prev = node.prev
            if prev.freq == freq - 1:
                prev.keys.add(key)
                self.map[key] = prev
            else:
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                prev.next = new_node
                new_node.prev = prev
                new_node.next = node
                node.prev = new_node
                self.map[key] = new_node
        else:
            new_node = Node(freq - 1)
            new_node.keys.add(key)
            new_node.next = node
            node.prev = new_node
            self.head = new_node
            self.map[key] = new_node
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail:
            key_set = self.tail.keys
            max_key = key_set.pop()
            key_set.add(max_key)
            return max_key
        else:
            return ""

    def getMinKey(self) -> str:
        if self.head:
            key_set = self.head.keys
            min_key = key_set.pop()
            key_set.add(min_key)
            return min_key
        else:
            return ""
    
    def removeNode(self, node: Node) -> None:
        if node == self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            else:
                self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            if not self.tail:
                self.head = None
            else:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
