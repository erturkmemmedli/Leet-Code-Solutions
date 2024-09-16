class Solution {
    public int[][] findFarmland(int[][] land) {
        int m = land.length, n = land[0].length;
        List<int[]> output = new ArrayList<>();
        int[][] directions = {{0,-1}, {0,1}, {-1,0}, {1,0}};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1) {
                    int r1 = i, c1 = j, r2 = i, c2 = j;
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[] {i, j});
                    land[i][j] = 0;
                    
                    while (!queue.isEmpty()) {
                        int[] coordinate = queue.remove();
                        int x = coordinate[0], y = coordinate[1];
                        r2 = Math.max(r2, x);
                        c2 = Math.max(c2, y);

                        for (int[] dir: directions) {
                            int row = x + dir[0], col = y + dir[1];

                            if (row >= 0 && row < m && col >= 0 && col < n && land[row][col] == 1) {
                                land[row][col] = 0;
                                queue.add(new int[] {row, col});
                            }
                        }
                    }

                    output.add(new int[] {r1, c1, r2, c2});
                }
            }
        }

        return output.toArray(new int[output.size()][4]);
    }
}
