class Solution {
    public int totalSteps(int[] nums) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] {nums[0], 0});
        int count = 0;

        for (int i = 1; i < nums.length; i++) {
            int temp = 0;

            while (!stack.isEmpty() && nums[i] >= stack.peek()[0]) {
                temp = Math.max(temp, stack.peek()[1]);
                stack.pop();
            }

            if (stack.isEmpty()) {
                temp = 0;
            } else {
                temp++;
            }

            count = Math.max(count, temp);
            stack.push(new int[] {nums[i], temp});
        }

        return count;
    }
}
