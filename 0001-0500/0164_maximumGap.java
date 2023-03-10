class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }
        Arrays.sort(nums);
        int maxDiff = 0;
        for (int i = 1; i < nums.length; i++) {
            maxDiff = Math.max(maxDiff, nums[i] - nums[i - 1]);
        }
        return maxDiff;
    }
}
