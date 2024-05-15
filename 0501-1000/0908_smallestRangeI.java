class Solution {
    public int smallestRangeI(int[] nums, int k) {
        List<Integer> res = findMinMax(nums);
        int min = res.get(0) + k;
        int max = res.get(1) - k;
        return min >= max ? 0 : max - min;
    }

    public List<Integer> findMinMax(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num: nums) {
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }

        return Arrays.asList(min, max);
    }
}
