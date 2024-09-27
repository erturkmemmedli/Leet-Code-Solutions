class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        int[] range = new int[2];
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            heap.offer(new int[] {nums.get(i).get(0), i, 0});
            min = Math.min(min, nums.get(i).get(0));
            max = Math.max(max, nums.get(i).get(0));
        }

        range[0] = min;
        range[1] = max;

        while (true) {
            int[] popped = heap.poll();

            if (popped[2] + 1 == nums.get(popped[1]).size() || heap.size() == 0) {
                return range;
            }

            heap.offer(new int[] {nums.get(popped[1]).get(popped[2] + 1), popped[1], popped[2] + 1});

            min = heap.peek()[0];
            max = Math.max(max, nums.get(popped[1]).get(popped[2] + 1));

            if (max - min < range[1] - range[0]) {
                range[0] = min;
                range[1] = max;
            }
        }
    }
}
