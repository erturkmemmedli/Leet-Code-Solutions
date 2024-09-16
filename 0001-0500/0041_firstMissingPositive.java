class Solution {
    public int firstMissingPositive(int[] nums) {
        int i = 0;
        int temp;

        while (i < nums.length) {
            while (0 < nums[i] && nums[i] <= nums.length && i + 1 != nums[i] && nums[i] != nums[nums[i] - 1]) {
                temp = nums[i];
                nums[i] = nums[temp - 1];
                nums[temp - 1] = temp;
            }
            i++;
        }

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j + 1) {
                return j + 1;
            }
        }

        return nums.length + 1;
    }
}