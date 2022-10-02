class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        self.impossible = 0
        for i in range(len(target)):
            if target[i] == '0':
                self.checkImpossible(deadends, target, i, 1, 9)
            elif target[i] == '9':
                self.checkImpossible(deadends, target, i, -1, -9)
            else:
                self.checkImpossible(deadends, target, i, 1, -1)   
        if self.impossible == 8:
            return -1
        return self.bfs(deadends, target)
        
    def checkImpossible(self, deadends, target, index, a, b):
        if target[:index] + chr(ord(target[index]) + a) + target[index+1:] in deadends:
            self.impossible += 1
        if target[:index] + chr(ord(target[index]) + b) + target[index+1:] in deadends:
            self.impossible += 1
        
    def bfs(self, deadends, target):
        queue = collections.deque([["0000"]])
        visited = set()
        level = 0
        while queue:
            lock = queue.popleft()
            new_lock = []
            for current in lock:
                if current == target:
                    return level
                if current not in visited:
                    visited.add(current)
                    for i in range(len(current)):
                        if current[i] == '0':
                            self.bfsQueueChecker(new_lock, visited, deadends, current, i, 1, 9)
                        elif current[i] == '9':
                            self.bfsQueueChecker(new_lock, visited, deadends, current, i, -1, -9)
                        else:
                            self.bfsQueueChecker(new_lock, visited, deadends, current, i, 1, -1)
            if new_lock:
                level += 1
                queue.append(new_lock)
        return -1

    def bfsQueueChecker(self, queue, visited, deadends, current, index, a, b):
        up = current[:index] + chr(ord(current[index]) + a) + current[index+1:] 
        down = current[:index] + chr(ord(current[index]) + b) + current[index+1:]
        if up not in deadends and up not in visited:
            queue.append(up)
        if down not in deadends and down not in visited:
            queue.append(down)
