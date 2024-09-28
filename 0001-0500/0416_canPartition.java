class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for (int num: nums) 
            sum += num;

        if (sum % 2 == 1) 
            return false;

        return dp(nums, new HashMap<>(), sum / 2, 0, 0);
    }

    public boolean dp(int[] nums, HashMap<String, Boolean> memo, int target, int current, int index) {
        if (current > target) 
            return false;

        if (current == target) 
            return true;

        if (index == nums.length) {
            return false;
        }

        if (memo.containsKey(current + "," + index))
            return memo.get(current + "," + index);

        boolean result = false;
        result = result || dp(nums, memo, target, current + nums[index], index + 1);
        result = result || dp(nums, memo, target, current, index + 1);

        memo.put(current + "," + index, result);
        return result;
    }
}
