class Solution {
    public long findTheArrayConcVal(int[] nums) {
        int mid = nums.length/2;
        long result = 0;

        for (int i=0; i < mid; i++) {
            result += Long.valueOf(String.valueOf(nums[i]) + String.valueOf(nums[nums.length-i-1]));
        }

        if (nums.length % 2 == 1) {
            result += (long) nums[mid];
        } 

        return result;
    }
}
