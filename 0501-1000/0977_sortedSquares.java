class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int deep = -1;

        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] * nums[i];
        }

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                deep = i - 1;
                break;
            }
        }

        if (deep == -1) {
            deep = n - 1;
        }

        result[0] = nums[deep];

        int idx = 1;
        int i = deep - 1;
        int j = deep + 1;

        while(i >= 0 && j < n) {
            if (nums[i] <= nums[j]) {
                result[idx] = nums[i];
                i--;
            } else {
                result[idx] = nums[j];
                j++;
            }
            idx++;
        }

        while (i >= 0) {
            result[idx] = nums[i];
            i--;
            idx++;
        }

        while (j < n) {
            result[idx] = nums[j];
            j++;
            idx++;
        }

        return result;
    }

}
