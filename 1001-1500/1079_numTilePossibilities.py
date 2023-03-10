class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        out = set()
        path = ''
        self.dfs(tiles, out, path)
        return len(out) - 1
        
    def dfs(self, tiles, out, path):
        out.add(path)
        for i in range(len(tiles)):
            self.dfs(tiles[i+1:] + tiles[:i], out, path + tiles[i])
        return
