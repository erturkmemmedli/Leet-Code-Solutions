class Solution {
    public List<List<Integer>> subsets(int[] nums) {
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
            path.add(nums[i]);
            backtrack(nums, output, path, i + 1);
            path.remove(path.size() - 1); 
        }
    }
}

// Alternative solution

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        output.add(new ArrayList<>());

        for (int num: nums) {
            int n = output.size();
            for (int i = 0; i < n; i++) {
                List<Integer> newList = new ArrayList<>(output.get(i));
                newList.add(num);
                output.add(newList);
            }
        }

        return output;
    }
}
