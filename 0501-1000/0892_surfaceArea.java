class Solution {
    public int surfaceArea(int[][] grid) {
        int surface = 0;
        int n = grid.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    surface += 2;
                }

                if (i - 1 < 0) {
                    surface += grid[i][j];
                } else {
                    surface += Math.max(0, grid[i][j] - grid[i - 1][j]);
                }

                if (i + 1 == n) {
                    surface += grid[i][j];
                } else {
                    surface += Math.max(0, grid[i][j] - grid[i + 1][j]);
                }
                
                if (j - 1 < 0) {
                    surface += grid[i][j];
                } else {
                    surface += Math.max(0, grid[i][j] - grid[i][j - 1]);
                }

                if (j + 1 == n) {
                    surface += grid[i][j];
                } else {
                    surface += Math.max(0, grid[i][j] - grid[i][j + 1]);
                }
            }
        }

        return surface;
    }
}
