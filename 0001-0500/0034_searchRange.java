class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] positions = {-1, -1};

        positions[0] = binarySearch(nums, target, true);
        positions[1] = binarySearch(nums, target, false);
        
        return positions;
    }

    public int binarySearch(int[] nums, int target, boolean leftSide) {
        int targetIndex = -1;
        int low = 0;
        int high = nums.length - 1;
        int mid;
        
        while (low <= high) {
            mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                targetIndex = mid;
                if (leftSide) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return targetIndex;
    }
}
