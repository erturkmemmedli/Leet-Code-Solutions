class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                visited.add(i)
                temp = [i]
                self.dfs(isConnected, n, i, visited, temp)
                result += 1
        return result
        
    def dfs(self, isConnected, n, i, visited, temp):
        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                temp.append(j)
                self.dfs(isConnected, n, j, visited, temp)
