class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length + 2];
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 0; i < nums.length; i++) {
            dp[i+2] = Math.max(dp[i+1], dp[i] + nums[i]);
        }
        return dp[nums.length + 1];
    }
}
