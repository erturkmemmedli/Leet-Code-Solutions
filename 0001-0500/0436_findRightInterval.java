class Solution {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int[][] modified = new int[n][3];
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            modified[i][0] = intervals[i][0];
            modified[i][1] = intervals[i][1];
            modified[i][2] = i;
        }

        for (int i = 0; i < n; i++) {
            result[i] = -1;
        }

        Arrays.sort(modified, (a, b) -> a[0] - b[0]);
        
        for (int i = 0; i < n; i++) {
            int start = modified[i][0];
            int end = modified[i][1];
            int index = modified[i][2];

            heap.offer(new int[] {end, index});

            while (!heap.isEmpty() && heap.peek()[0] <= start) {
                int[] pop = heap.poll();
                result[pop[1]] = index;
            }
        }

        return result;
    }
}
