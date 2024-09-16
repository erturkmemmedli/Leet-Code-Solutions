class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            int index = binarySearch(list, nums[i]);

            if (index == list.size()) {
                list.add(nums[i]);
            } else {
                list.set(index, nums[i]);
            }
        }

        return list.size();
    }

    public int binarySearch(List<Integer> list, int target) {
        int low = 0;
        int high = list.size() - 1;
        int mid;

        while (low <= high) {
            mid = low + (high - low) / 2;
            
            if (list.get(mid) >= target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }
}
