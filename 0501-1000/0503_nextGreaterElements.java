class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] modifiedNums = new int[2*n-1];
        int[] result = new int[n];

        for (int i=0; i<n; i++) {
            modifiedNums[i] = nums[i];
        }
        for (int i=0; i<n-1; i++) {
            modifiedNums[n+i] = nums[i];
        }

        Stack<Integer> stack = new Stack<>();
        
        for (int i=2*n-2; i>=0; i--) {
            while (!stack.empty() && stack.peek()<=modifiedNums[i]) {
                stack.pop();
            }

            if (i < n) {
                result[i] = stack.empty() ? -1 : stack.peek();
            }

            stack.push(modifiedNums[i]);
        }

        return result;
    }
}
