class Solution {
    public boolean isBoomerang(int[][] points) {
        int[] first = points[0];
        int[] second = points[1];
        int[] third = points[2];

        int slope1 = (third[1] - second[1]) * (second[0] - first[0]);
        int slope2 = (second[1] - first[1]) * (third[0] - second[0]);

        return slope1 != slope2;
    }
}
