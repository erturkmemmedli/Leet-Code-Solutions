class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int currentColor = image[sr][sc];

        if (currentColor == color) return image;

        int m = image.length, n = image[0].length;
        Queue<int[]> queue = new LinkedList<>(){{add(new int[] {sr, sc});}};
        int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0, 1}};

        while (!queue.isEmpty()) {
            int[] coordinate = queue.remove();
            int x = coordinate[0], y = coordinate[1];
            image[x][y] = color;

            for (int[] direction: directions) {
                int r = x+direction[0], c = y+direction[1];
                if (0 <= r && r < m && 0 <= c && c < n && image[r][c] == currentColor) {
                    image[r][c] = color;
                    queue.add(new int[] {r, c});
                }
            }
        }

        return image;
    }
}
