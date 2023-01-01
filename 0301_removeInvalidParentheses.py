class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = collections.deque([[s]])
        answer = []
        visited = set()
        while queue:
            strings = queue.popleft()
            nextLevel = []
            for string in strings:
                if self.isValidString(string):
                    answer.append(string)
                if not answer:
                    for i in range(len(string)):
                        if string[i] in ['(', ')']:
                            candidate = string[:i] + string[i+1:]
                            if candidate not in visited:
                                visited.add(candidate)
                                nextLevel.append(candidate)
            if nextLevel:
                queue.append(nextLevel)
        return answer

    def isValidString(self, s):
        hashmap = {'(': 1, ')': -1}
        count = 0
        for i in range(len(s)):
            count += hashmap.get(s[i], 0)
            if count < 0:
                return False
        return count == 0
