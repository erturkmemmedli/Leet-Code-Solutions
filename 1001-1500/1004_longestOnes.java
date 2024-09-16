class Solution {
    public int longestOnes(int[] nums, int k) {
        int max = 0;
        int left = 0;
        int right = 0;

        while (right < nums.length) {
            if (nums[right] == 1 || (nums[right] == 0 && k > 0)) {
                if (nums[right] == 0) k--;
                right++;
                max = Math.max(max, right - left);
            } 

            while (right < nums.length && nums[right] == 0 && k == 0) {
                if (nums[left] == 0) k++;
                left++;
            }
        }

        max = Math.max(max, right - left);
        return max;
    }
}
