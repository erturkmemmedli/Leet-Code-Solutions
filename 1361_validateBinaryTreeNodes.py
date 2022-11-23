class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1:
                if parent[l] == -1:
                    parent[l] = i
                else:
                    return False
            if r != -1:
                if parent[r] == -1:
                    parent[r] = i
                else:
                    return False
        if parent.count(-1) != 1:
            return False
        for i in range(n):
            visited = set()
            if not self.find(i, parent, visited):
                return False
        return True

    def find(self, i, parent, visited):
        if i not in visited:
            if parent[i] != -1:
                visited.add(i)
                return self.find(parent[i], parent, visited)
            return True
        else:
            return False
            
# Alternative solution

class Solution1:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1:
                if parent[l] == -1:
                    parent[l] = i
                else:
                    return False
            if r != -1:
                if parent[r] == -1:
                    parent[r] = i
                else:
                    return False
        if parent.count(-1) != 1:
            return False
        for i in range(n):
            if parent[i] != -1:
                if not self.find(i, parent, set()):
                    return False
        return True

    def find(self, i, parent, visited):
        if i not in visited:
            if parent[i] != -1:
                visited.add(i)
                parent[i] = self.find(parent[i], parent, visited)
            if parent[i] != None:
                return -1
        else:
            return None
