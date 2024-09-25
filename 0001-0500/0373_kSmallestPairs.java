class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int m = nums1.length, n = nums2.length;
        List<List<Integer>> output = new ArrayList<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        for (int i = 0; i < n; i++) {
            heap.offer(new int[] {nums1[0] + nums2[i], 0, i});
        }

        while (true) {
            int[] pair = heap.poll();
            k--;
            output.add(new ArrayList<>() {{
                add(nums1[pair[1]]); 
                add(nums2[pair[2]]);
            }});

            if (k == 0) {
                return output;
            }

            if (pair[1] + 1 < m) {
                heap.offer(new int[] {nums1[pair[1] + 1] + nums2[pair[2]], pair[1] + 1, pair[2]});
            }
        }
    }
}
