class Solution {
    public void sortColors(int[] nums) {
        int i = 0;
        int j = 0;
        int k = 0;
        int temp;

        while (k < nums.length) {
            if (nums[k] == 2) {
                k++;
            } else if (nums[k] == 1) {
                temp = nums[j];
                nums[j] = nums[k];
                nums[k] = temp;
                j++;
                k++;
            } else {
                temp = nums[j];
                nums[j] = nums[k];
                nums[k] = temp;
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
                k++;
            }
        }
    }
}
