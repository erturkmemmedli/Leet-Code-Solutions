class Solution {
    public int minimumOperations(int[] nums) {
        PriorityQueue<Integer> heap = new PriorityQueue();
        int step = 0;

        for (int num: nums) {
            if (num != 0) {
                heap.add(num);
            }
        }

        while (!heap.isEmpty()) {
            PriorityQueue<Integer> temp = new PriorityQueue();
            int minimum = heap.poll();
            step++;
            
            for (int num: heap) {
                if (num - minimum != 0) {
                    temp.add(num - minimum);
                }
            }

            heap = temp;
        }

        return step;
    }
}
