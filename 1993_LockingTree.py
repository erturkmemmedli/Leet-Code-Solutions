class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [set() for _ in range(len(parent))]
        for child, father in enumerate(parent):
            if father == -1:
                continue
            self.children[father].add(child)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        if self.lockedAncestor(num):
            return False
        if not self.lockedDescendant(num):
            return False
        else:
            self.unlockAllDecendants(num)
            self.locked[num] = user
            return True

    def lockedAncestor(self, num):
        if num == -1:
            return False
        if num in self.locked:
            return True
        return self.lockedAncestor(self.parent[num])
    
    def lockedDescendant(self, num):
        queue = collections.deque([num])
        while queue:
            node = queue.popleft()
            for child in self.children[node]:
                if child in self.locked:
                    return True
                queue.append(child)
        return False

    def unlockAllDecendants(self, num):
        if not self.children[num]:
            if num in self.locked:
                del self.locked[num]
            return
        for child in self.children[num]:
            if child in self.locked:
                del self.locked[child]
            self.unlockAllDecendants(child)

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
