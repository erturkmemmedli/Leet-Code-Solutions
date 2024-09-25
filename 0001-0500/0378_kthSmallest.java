class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int i = 0; i < m; i++) {
            heap.offer(new int[] {matrix[i][0], i, 0});
        }

        while (true) {
            int[] pair = heap.poll();
            k--;

            if (k == 0) {
                return pair[0];
            }

            if (pair[2] + 1 < n) {
                heap.offer(new int[] {matrix[pair[1]][pair[2] + 1], pair[1], pair[2] + 1});
            }
        }
    }
}
