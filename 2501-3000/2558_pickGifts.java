class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

        for (int num: gifts) {
            heap.offer(num);
        }

        while (k > 0) {
            heap.offer((int) Math.floor(Math.sqrt(heap.poll())));
            k--;
        }

        long sum = 0;

        for (int num: heap) {
            sum += num;
        }

        return sum;
    }
}
