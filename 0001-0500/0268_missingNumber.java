class Solution {
    public int missingNumber(int[] nums) {
        int i = 0;
        int temp;

        while (i < nums.length) {
            while (nums[i] != nums.length && i != nums[i]) {
                temp = nums[i];
                nums[i] = nums[nums[i]];
                nums[temp] = temp;
            }
            i++;
        }

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j) {
                return j;
            }
        }

        return nums.length;
    }
}
