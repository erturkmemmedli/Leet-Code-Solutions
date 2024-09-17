class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxArea = 0;
        int maxDiagonal = 0;

        for (int[] dimension: dimensions) {
            int l = dimension[0];
            int w = dimension[1];
            int d = l * l + w * w;

            if (d > maxDiagonal) {
                maxDiagonal = d;
                maxArea = l * w;
            } else if (d == maxDiagonal) {
                maxArea = Math.max(maxArea, l * w);
            }
        }

        return maxArea;
    }
}
