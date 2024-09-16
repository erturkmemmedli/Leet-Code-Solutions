class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicates = new ArrayList<>();
        int i = 0;
        int temp;

        while (i < nums.length) {
            while (nums[i] != i + 1 && nums[i] != nums[nums[i] - 1]) {
                temp = nums[i];
                nums[i] = nums[nums[i] - 1];
                nums[temp - 1] = temp;
            }
            i++;
        }

        for (int j = 0; j < nums.length; j++) {
            if (j != nums[j] - 1) {
                duplicates.add(nums[j]);
            }
        }

        return duplicates;
    }
}
