class Solution {
    public boolean increasingTriplet(int[] nums) {
        int a = Integer.MIN_VALUE;
        int b = Integer.MIN_VALUE;
        int c = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (a == Integer.MIN_VALUE) {
                a = nums[i];
            } else if (b == Integer.MIN_VALUE) {
                if (nums[i] <= a) {
                    a = nums[i];
                } else {
                    b = nums[i];
                }
            } else if (c  == Integer.MIN_VALUE) {
                if (nums[i] <= a) {
                    a = nums[i];
                } else if (nums[i] <= b) {
                    b = nums[i];
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}
