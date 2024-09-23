class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        int[][] combined = new int[n][2];

        for (int i = 0; i < n; i++) {
            combined[i][0] = profits[i];
            combined[i][1] = capital[i];
        }

        Arrays.sort(combined, (a, b) -> a[1] - b[1]);
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int i = 0;

        while (i < profits.length && k > 0) {
            while (i < n && combined[i][1] <= w) {
                heap.offer(new int[] {-combined[i][0], combined[i][1]});
                i++;
            }

            if (heap.isEmpty()) {
                break;
            }

            if (!heap.isEmpty() && k > 0) {
                int[] pop = heap.poll();
                w -= pop[0];
                k--;
            }
        }

        while (!heap.isEmpty() && k > 0) {
            int[] pop = heap.poll();
            w -= pop[0];
            k--;
        }

        return w;
    }
}
