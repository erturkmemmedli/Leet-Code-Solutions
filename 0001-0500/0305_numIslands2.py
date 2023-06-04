class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]

        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        self.parent[root2] = root1

        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        island_counts = []
        count = 0

        for i, [row, col] in enumerate(positions):
            if (row, col) not in uf.parent:
                uf.parent[(row, col)] = (row, col)
                count += 1

            for r, c in [row - 1, col], [row, col - 1], [row + 1, col], [row, col + 1]:
                if (r, c) in uf.parent:
                    if uf.union((row, col), (r, c)):
                        count -= 1

            island_counts.append(count)

        return island_counts

# ALternative solution (which gives TLE error)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        islands = []
        num_of_islands = []

        for r, c in positions:
            possible_merges = []
            existing_land = False

            for island in islands:
                if (r, c ) in island:
                    num_of_islands.append(len(islands))
                    existing_land = True
                    break

            if existing_land:
                continue

            for row, col in [r-1, c], [r, c-1], [r+1, c], [r, c+1]:
                if m > row >= 0 <= col < n:
                    for i, island in enumerate(islands):
                        if (row, col) in island:
                            island.add((r, c))
                            possible_merges.append(i)
                            break
                        
            if len(possible_merges) == 0:
                islands.append({(r, c)})
                
            if len(possible_merges) > 1:
                for i in range(1, len(possible_merges)):
                    islands[possible_merges[0]] |= islands[possible_merges[i]]

                new_islands = [islands[possible_merges[0]]]

                for i, island in enumerate(islands):
                    if i not in possible_merges:
                        new_islands.append(island)

                islands = new_islands

            num_of_islands.append(len(islands))

        return num_of_islands
