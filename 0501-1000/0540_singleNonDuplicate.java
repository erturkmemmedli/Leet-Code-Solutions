class Solution {
    public int singleNonDuplicate(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        int mid;

        while (low < high) {
            mid = low + (high - low) / 2;

            if ((high - low + 1) % 4 == 1) {
                if (nums[mid] == nums[mid - 1]) {
                    high = mid - 2;
                } else {
                    low = mid;
                }
            } else {
                if (nums[mid] == nums[mid - 1]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        return nums[low];
    }
}
