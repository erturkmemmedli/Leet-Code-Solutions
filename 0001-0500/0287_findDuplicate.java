class Solution {
    public int findDuplicate(int[] nums) {
        int i = 0;
        int temp;

        while (i < nums.length) {
            while (nums[i] != i + 1 && nums[i] != nums[nums[i] - 1]) {
                temp = nums[i];
                nums[i] = nums[nums[i] - 1];
                nums[temp - 1] = temp;
            }

            if (nums[i] != i + 1 && nums[i] == nums[nums[i] - 1]) {
                return nums[i];
            }

            i++;
        }

        return -1;
    }
}
