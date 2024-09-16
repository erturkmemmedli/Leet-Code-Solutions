class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        int temp;

        while (j < nums.length) {
            if (nums[j] == 0) {
                j++;
            } else {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
            }
        }
    }
}
