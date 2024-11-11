class Solution {
    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length, n = rooms[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    queue.add(new int[] {i, j});
                }
            }
        }
        
        while (!queue.isEmpty()) {
            int[] node = queue.remove();
            int x = node[0], y = node[1];
            
            for (int[] dir: directions) {
                int r = x + dir[0], c = y + dir[1];
                
                if (r >= 0 && r < m && c >= 0 && c < n && rooms[r][c] > rooms[x][y]) {
                    rooms[r][c] = rooms[x][y] + 1;
                    queue.add(new int[] {r, c});
                }
            }
        }
    }
}
