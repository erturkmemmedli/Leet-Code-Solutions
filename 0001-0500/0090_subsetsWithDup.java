class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<>();
        backtrack(nums, output, new ArrayList<>(), 0);
        return output;
    }

    public void backtrack(int[] nums, List<List<Integer>> output, List<Integer> path, int index) {
        output.add(new ArrayList<>(path));

        if (index == nums.length) {
            return;
        }

        for (int i = index; i < nums.length; i++) {
            if (i > index && nums[i] == nums[i - 1]) {
                continue;
            }
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(nums[i]);
            backtrack(nums, output, newPath, i + 1);
            newPath.remove(newPath.size() - 1);
        }
    }
}
