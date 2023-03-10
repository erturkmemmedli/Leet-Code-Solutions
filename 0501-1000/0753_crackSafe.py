class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        string = "0" * (n-1)
        visited = set()
        result = string
        while True:
            for i in range(k-1, -1, -1):
                if (string, i) not in visited:
                    result += str(i)
                    visited.add((string, i))
                    string = (string + str(i))[1:]
                    break
            else:
                return result
