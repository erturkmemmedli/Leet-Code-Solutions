class Solution {
    public long coloredCells(int n) {
        int k = 2 * n - 1;
        long result = k;

        for (int i = 1; i < k; i += 2) {
            result += i * 2;
        }

        return result;
    }
}
