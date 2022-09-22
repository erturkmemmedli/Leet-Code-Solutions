class TrieNode:
    def __init__(self, val = None):
        self.children = {}
        self.val = val

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key not in self.map:
            self.map[key] = val           
            for char in key:
                if char not in node.children:
                    node.children[char] = TrieNode(val)
                else:
                    node.children[char].val += val
                node = node.children[char]
        else:
            old_val = self.map[key]
            self.map[key] = val
            for char in key:
                node.children[char].val += val - old_val
                node = node.children[char]
            
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            if node.children:
                node = node.children[char]
        return node.val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
