class Solution {
    public int thirdMax(int[] nums) {
        int[] mxm = {Integer.MAX_VALUE, 0};
        int[] first = maximum(nums, mxm[0], 0);
        int[] second = maximum(nums, first[0], 0);
        if (second[1] == 0) {
            return first[0];
        }
        int[] third = maximum(nums, second[0], 0);
        if (third[1] == 0) {
            return first[0];
        }
        return third[0];
    }
    
    public int[] maximum(int[] nums, int max, int count) {
        int temp = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= temp && nums[i] < max) {
                temp = nums[i];
                count ++;
            }
        }
        int[] res = {temp, count};
        return res;
    }
}
