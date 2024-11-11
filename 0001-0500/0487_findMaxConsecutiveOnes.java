class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;

        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];

            if (num != 1) {
                zeroCount++;

                while (zeroCount > 1) {
                    if (nums[left] == 0) {
                        zeroCount--;
                    }

                    left++;
                }
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
