class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        backtrack(nums, output, new ArrayList<>(), new boolean[nums.length]);
        return output;
    }
    
    public void backtrack(int[] nums, List<List<Integer>> output, List<Integer> path, boolean[] used) {
        if (path.size() == nums.length) {
            output.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i] == true) {
                continue;
            }
            used[i] = true;
            path.add(nums[i]);
            backtrack(nums, output, path, used);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
