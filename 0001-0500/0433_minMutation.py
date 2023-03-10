class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # construction of graph
        graph = collections.defaultdict(list)
        for word in bank:
            if self.isOneLetterDifferent(start, word):
                graph[start].append(word)
        for i in range(len(bank)):
            for j in range(len(bank)):
                if i != j:
                    if self.isOneLetterDifferent(bank[i], bank[j]):
                        graph[bank[i]].append(bank[j])
                        graph[bank[j]].append(bank[i])
        # breadth-first search
        queue = collections.deque([(start, 0)])
        visited = set()
        while queue:
            node, index = queue.popleft()
            if node == end:
                return index
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, index + 1))
        return -1

    def isOneLetterDifferent(self, word1, word2):
        difference = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
            if difference > 1:
                return False
        return difference == 1
