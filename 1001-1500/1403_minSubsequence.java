class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        int n = nums.length;
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }

        Arrays.sort(nums);
        List<Integer> output = new ArrayList<>();
        int curr = 0;

        for (int j = n-1; j >= 0; j--) {
            curr += nums[j];
            output.add(nums[j]);

            if (curr > sum / 2) {
                break;
            }
        }

        return output;
    }
}
