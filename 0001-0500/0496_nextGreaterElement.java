class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;

        HashMap<Integer, Integer> nextGreater = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        int[] resultSet = new int[n1];

        for (int i = n2 - 1; i >= 0; i--) {
            while (!stack.empty() && stack.peek() <= nums2[i]) {
                stack.pop();
            }

            if (stack.empty()) {
                nextGreater.put(nums2[i], -1);
            } else {
                nextGreater.put(nums2[i], stack.peek());
            }

            stack.push(nums2[i]);
        }

        for (int i = 0; i < n1; i++) {
            resultSet[i] = nextGreater.get(nums1[i]);
        }

        return resultSet;
    }
}
