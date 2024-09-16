class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        PriorityQueue<int[]> pQueue = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) return a[1] - b[1];
            else return b[0] - a[0];
        });

        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        counter.forEach((num, count) -> pQueue.add(new int[]{num, count}));

        int i = 0;

        while (!pQueue.isEmpty()) {
            int[] pair = pQueue.poll();

            for (int j = 0; j < pair[1]; j++) {
                nums[i] = pair[0];
                i++;
            }
        }

        return nums;
    }
}
