class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int firstIndex; int secondIndex; int thirdIndex;

        for (int i = 0; i < nums.length; i++) {
            while (i > 0 && i < nums.length && nums[i] == nums[i - 1]) {
                i++;
            }


            firstIndex = i;
            secondIndex = i + 1;
            thirdIndex = nums.length - 1;

            while (secondIndex < thirdIndex) {
                if (nums[firstIndex] + nums[secondIndex] + nums[thirdIndex] == 0) {
                    List<Integer> pairs = new ArrayList<>();
                    pairs.add(nums[firstIndex]);
                    pairs.add(nums[secondIndex]);
                    pairs.add(nums[thirdIndex]);
                    result.add(pairs);
                    secondIndex++;
                    while (secondIndex < nums.length && nums[secondIndex] == nums[secondIndex - 1]) {
                        secondIndex++;
                    }
                    thirdIndex--;
                    while (thirdIndex >= 0 && nums[thirdIndex] == nums[thirdIndex + 1]) {
                        thirdIndex--;
                    }
                } else if (nums[firstIndex] + nums[secondIndex] + nums[thirdIndex] < 0) {
                    secondIndex++;
                    while (secondIndex < nums.length && nums[secondIndex] == nums[secondIndex - 1]) {
                        secondIndex++;
                    }
                } else {
                    thirdIndex--;
                    while (thirdIndex >= 0 && nums[thirdIndex] == nums[thirdIndex + 1]) {
                        thirdIndex--;
                    }
                }
                
            }
        }

        return result;
    }
}
