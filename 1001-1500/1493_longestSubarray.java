class Solution {
    public int longestSubarray(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        int longest = 0;
        boolean zeroExists = false;
        int one = 0;
        int zero = 0;

        for (int num: nums) {
            if (num == 1) {
                zero = 0;
                one++;
            } else {
                zeroExists = true;
                zero++;
                if (zero == 1) {
                    arr.add(one);
                    one = 0;
                } else if (arr.get(arr.size() - 1) != 0) {
                    arr.add(0);
                }
            }
        }

        arr.add(one);
        longest = arr.get(0);

        for (int i = 1; i < arr.size(); i++) {
            longest = Math.max(longest, arr.get(i - 1) + arr.get(i));
        }

        return (zeroExists) ? longest : longest - 1;
    }
}
