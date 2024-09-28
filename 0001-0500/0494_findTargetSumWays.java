class Solution {
    public HashMap<String, Integer> memo = new HashMap<>();

    public int findTargetSumWays(int[] nums, int target) {
        return dp(nums, target, 0, 0);
    }

    public int dp(int[] nums, int target, int current, int index) {
        if (index == nums.length) {
            return (current == target) ? 1 : 0;
        }

        if (memo.containsKey(current + "," + index)) {
            return memo.get(current + "," + index);
        }

        int total = 0;

        total += dp(nums, target, current + nums[index], index + 1);
        total += dp(nums, target, current - nums[index], index + 1);

        memo.put(current + "," + index, total);
        return total;
    }
}
