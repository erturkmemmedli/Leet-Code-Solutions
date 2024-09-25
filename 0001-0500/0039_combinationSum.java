class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> output = new ArrayList<>();
        backtrack(candidates, target, output, new ArrayList<>(), 0, 0);
        return output;
    }

    public void backtrack(int[] candidates, int target, List<List<Integer>> output, List<Integer> path, int sum, int idx) {
        if (sum == target) {
            output.add(new ArrayList<>(path));
        }

        for (int i = idx; i < candidates.length; i++) {
            if (sum + candidates[i] <= target) {
                path.add(candidates[i]);
                backtrack(candidates, target, output, path, sum + candidates[i], i);
                path.remove(path.size() - 1);
            }
        }
    }
}
