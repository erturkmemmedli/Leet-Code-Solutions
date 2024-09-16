class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int m = grid2.length, n = grid2[0].length;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid2[i][j] == 1) {
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[] {i, j});
                    grid2[i][j] = 0;
                    boolean countable = (grid1[i][j] == 1);

                    while (!queue.isEmpty()) {
                        int[] coordinate = queue.remove();
                        int x = coordinate[0], y = coordinate[1];
                        if (grid1[x][y] == 0) {
                            countable = false;
                        }

                        for (int[] dir: directions) {
                            int r = x + dir[0], c = y + dir[1];
                            
                            if (r >= 0 && r < m && c>= 0 && c < n && grid2[r][c] == 1) {
                                grid2[r][c] = 0;
                                queue.add(new int[] {r, c});
                            }
                        }
                    }

                    count += (countable) ? 1 : 0;
                }
            }
        }

        return count;
    }
}
