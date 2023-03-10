class Solution:
    def simplifyPath(self, path: str) -> str:
        canonicalPath = []
        for i, char in enumerate(path):
            if not canonicalPath:
                canonicalPath.append(char)
                continue
            if char == '/':
                if canonicalPath[-1] == '/':
                    continue
                if len(canonicalPath) > 2 and canonicalPath[-3:] == ['/','.','.']:
                    canonicalPath.pop()
                    canonicalPath.pop()
                    canonicalPath.pop()
                    j = len(canonicalPath) - 1
                    while canonicalPath and canonicalPath[j] != '/':
                        j -= 1
                    canonicalPath = canonicalPath[:j]
                elif len(canonicalPath) > 1 and canonicalPath[-2:] == ['/','.']:
                    canonicalPath.pop()
                    canonicalPath.pop()
                if i < len(path) - 1:
                    canonicalPath.append(char)
            else:
                canonicalPath.append(char)
        if canonicalPath and canonicalPath[-1] == '/':
            canonicalPath.pop()
        if len(canonicalPath) > 2 and canonicalPath[-3:] == ['/','.','.']:
            canonicalPath.pop()
            canonicalPath.pop()
            canonicalPath.pop()
            j = len(canonicalPath) - 1
            while canonicalPath and canonicalPath[j] != '/':
                j -= 1
            canonicalPath = canonicalPath[:j]
        elif len(canonicalPath) > 1 and canonicalPath[-2:] == ['/','.']:
            canonicalPath.pop()
            canonicalPath.pop()         
        if not canonicalPath:
            canonicalPath.append('/')
        return "".join(canonicalPath)
