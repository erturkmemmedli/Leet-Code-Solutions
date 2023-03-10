class Solution:
    def minJumps(self, arr: List[int]) -> int:
        duplicates = collections.defaultdict(list)

        for i, num in enumerate(arr):
            duplicates[num].append(i)

        queue = deque([(0, 0)])
        same_elements = set()
        visited = set()

        while queue:
            distance, node = queue.popleft()

            if node == len(arr) - 1:
                return distance

            for neighbor in [node - 1, node + 1]:
                if 0 <= neighbor < len(arr) and neighbor not in visited:
                    queue.append((distance + 1, neighbor))
                    visited.add(neighbor)

            if arr[node] not in same_elements:
                for neighbor in duplicates[arr[node]]:
                    if neighbor not in visited:
                        queue.append((distance + 1, neighbor))
                        visited.add(neighbor)
                same_elements.add(arr[node])
