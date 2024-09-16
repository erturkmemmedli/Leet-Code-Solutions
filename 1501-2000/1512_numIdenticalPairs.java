class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> counterMap = new HashMap<>();
        for (int i=0; i<nums.length; i++) counterMap.put(nums[i], counterMap.getOrDefault(nums[i], 0) + 1);
        AtomicInteger result = new AtomicInteger(0);
        counterMap.forEach((key, val) -> result.getAndAdd(val * (val - 1) / 2));
        return result.get();
    }
}
