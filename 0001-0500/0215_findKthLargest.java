class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (int num: nums) {
            if (heap.size() < k) {
                heap.add(num);
                continue;
            }

            if (heap.peek() < num) {
                heap.poll();
                heap.add(num);
            }
        }

        return heap.peek();
    }
}
