class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> output = new ArrayList<>();
        int i = 0;
        int temp;

        while (i < nums.length) {
            while (i + 1 != nums[i] && nums[i] != nums[nums[i] - 1]) {
                temp = nums[i];
                nums[i] = nums[nums[i] - 1];
                nums[temp - 1] = temp;
            }
            i++;
        }

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j + 1) {
                output.add(j + 1);
            }
         }

         return output;
    }
}
