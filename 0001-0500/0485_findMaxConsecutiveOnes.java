class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int left = 0;
        int right = 0;

        while (right < nums.length) {
            if (nums[right] == 1) {
                right++;
                max = Math.max(max, right - left);
            } else {
                right++;
                left = right;
            }
        }

        max = Math.max(max, right - left);
        return max;
    }
}
