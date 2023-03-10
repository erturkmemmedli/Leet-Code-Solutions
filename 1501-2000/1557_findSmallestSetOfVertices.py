class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(0, n))
        for row, col in edges:
            nodes.discard(col)
        return nodes
