class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int numOfIslands = 0;
        Queue<int[]> queue;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    queue = new LinkedList<>();
                    queue.add(new int[] {i, j});
                    grid[i][j] = '@';
                    numOfIslands++;

                    while (!queue.isEmpty()) {
                        int[] coordinate = queue.remove();
                        int x = coordinate[0], y = coordinate[1];

                        for (int[] direction: directions) {
                            int r = direction[0], c = direction[1];

                            if (0 <= x+r && x+r < m && 0 <= y+c && y+c < n && grid[x+r][y+c] == '1') {
                                grid[x+r][y+c] = '@';
                                queue.add(new int[] {x+r, y+c});
                            }
                        }
                    }
                }
            }
        }

        return numOfIslands;
    }
}
