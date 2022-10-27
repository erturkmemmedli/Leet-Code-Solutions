class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return
        self.output = set()
        self.dfs(s, [])
        return self.output

    def dfs(self, string, path):
        if ".".join(path) not in self.output:
            if len(path) == 4:
                if any(len(i) == 0 for i in path):
                    return
                if any(len(i) > 3 for i in path):
                    return
                if any(len(i) > 1 and i[0] == '0' for i in path):
                    return
                if any(int(i) > 255 for i in path):
                    return
                else:
                    self.output.add(".".join(path))
                    return
            for _ in range(4):
                if len(path) < 3:
                    self.dfs(string[1:], path + [string[:1]])
                    self.dfs(string[2:], path + [string[:2]])
                    self.dfs(string[3:], path + [string[:3]])
                else:
                    self.dfs([], path + [string])

# Alternative solution
                    
class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return
        self.output = set()
        self.dfs(s, [])
        return self.output

    def dfs(self, string, path):
        if len(path) == 4 and ".".join(path) not in self.output:
            self.output.add(".".join(path))
            return
        for _ in range(4):
            if len(path) < 3:
                if not string:
                    return
                elif string[0] != '0':
                    self.dfs(string[1:], path + [string[:1]])
                    self.dfs(string[2:], path + [string[:2]])
                    if int(string[:3]) <= 255:
                        self.dfs(string[3:], path + [string[:3]])
                else:
                    self.dfs(string[1:], path + [string[:1]])
            else:
                if len(string) == 0 or len(string) > 3 or (len(string) > 1 and string[0] == '0') or int(string[:3]) > 255:
                    return
                else:
                    self.dfs([], path + [string])
