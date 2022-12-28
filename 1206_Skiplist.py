class ListNode:
    def __init__(self, val = None, next = None, down = None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self):
        self.skiplist = [ListNode()]

    def search(self, target: int) -> bool:
        current = self.skiplist[-1]
        while current:
            while current.next and current.next.val <= target:
                if current.next.val == target:
                    return True
                current = current.next
            else:
                current = current.down
        return False

    def add(self, num: int) -> None:
        level = 1
        r = random.choice([0, 1])
        while r == 1 and level < len(self.skiplist):
            level += 1
            r = random.choice([0, 1])
        if level == len(self.skiplist):
            newNode = ListNode()
            newNode.down = self.skiplist[-1]
            self.skiplist.append(newNode)
        current = self.skiplist[-1]
        stage = len(self.skiplist)
        parent = None
        while current:
            while current.next and current.next.val <= num:
                current = current.next
            if stage <= level:
                newNode = ListNode(num)
                newNode.next = current.next
                current.next = newNode
                if parent:
                    parent.down = newNode
                parent = newNode
            current = current.down
            stage -= 1

    def erase(self, num: int) -> bool:
        current = self.skiplist[-1]
        doesExist = False
        while current:
            while current.next and current.next.val <= num:
                if current.next.val == num:
                    doesExist = True
                    current.next = current.next.next
                    break
                current = current.next
            current = current.down
        while len(self.skiplist) > 1:
            if not self.skiplist[-2].next:
                self.skiplist.pop()
                continue
            break
        return doesExist

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
