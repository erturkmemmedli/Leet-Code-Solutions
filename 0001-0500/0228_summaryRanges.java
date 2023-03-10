class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }
        String temp = Integer.toString(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] + 1) {
                if (temp.length() < 3 || ! (temp.length() >= 3 && temp.substring(temp.length()-2, temp.length()).equals("->"))) {
                    temp += "->";
                }
            } else {
                if (temp.length() >= 3 && temp.substring(temp.length()-2, temp.length()).equals("->")) {
                    temp += Integer.toString(nums[i-1]);
                }
                result.add(temp);
                temp = Integer.toString(nums[i]);
            }
        }
        if (temp.length() >= 3 && temp.substring(temp.length()-2, temp.length()).equals("->"))  {
            temp += Integer.toString(nums[nums.length-1]);
        }
        result.add(temp);
        return result;
    }
}
