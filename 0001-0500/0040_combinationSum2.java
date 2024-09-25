class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> output = new ArrayList<>();
        backtrack(candidates, target, output, new ArrayList<>(), 0, 0);
        return output;
    }

    public void backtrack(int[] candidates, int target, List<List<Integer>> output, List<Integer> path, int sum, int idx) {
        if (sum == target) {
            output.add(new ArrayList<>(path));
        }

        for (int i = idx; i < candidates.length; i++) {
            if (i > idx && candidates[i] == candidates[i - 1]) {
                continue;
            }
            if (sum + candidates[i] <= target) {
                path.add(candidates[i]);
                backtrack(candidates, target, output, path, sum + candidates[i], i + 1);
                path.remove(path.size() - 1);
            }
        }
    }
}
