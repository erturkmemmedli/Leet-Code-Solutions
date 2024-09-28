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
            path.add(nums[i]);
            backtrack(nums, output, path, i + 1);
            path.remove(path.size() - 1);
        }
    }
}

// Alternative solution

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<>();
        output.add(new ArrayList<>());
        int n = nums.length;
        int end = 0;

        for (int i = 0; i < n; i++) {
            int start = 0;
            if (i > 0 && nums[i] == nums[i - 1]) {
                start = end + 1;
            }
            int k = output.size();
            end = k - 1;

            for (int j = start; j < end + 1; j++) {
                List<Integer> list = new ArrayList<>(output.get(j));
                list.add(nums[i]);
                output.add(list);
            }
        }

        return output;
    }
}
