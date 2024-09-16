class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num: nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }
        return false;
    }
}

// Alternative solution

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toCollection(HashSet::new));
        return nums.length != set.size();
    }
}
