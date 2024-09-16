class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<List<Integer>> stack = new Stack<>();
        int n = heights.length;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int height = heights[i];
            int width = 1;

            while (!stack.empty() && stack.peek().get(0) >= height) {
                List<Integer> x = stack.pop();

                if (!stack.empty() && stack.peek().get(0) >= height) {
                    List<Integer> y = stack.pop();
                    stack.push(List.of(y.get(0), y.get(1) + x.get(1)));
                    maxArea = Math.max(maxArea, stack.peek().get(0) * stack.peek().get(1));
                } else {
                    width += x.get(1);
                    maxArea = Math.max(maxArea, height * width);
                }
            }

            stack.push(List.of(height, width));
            maxArea = Math.max(maxArea, height * width);
        }

        int w = stack.pop().get(1);

        while (!stack.empty()) {
            List<Integer> z = stack.pop();
            w += z.get(1);
            maxArea = Math.max(maxArea, z.get(0) * w);
        }

        return maxArea;
    }
}

// Alternative solution

class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<List<Integer>> stack = new Stack<>();
        int n = heights.length;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int height = heights[i];
            int width = 0;

            while (!stack.empty() && stack.peek().get(0) >= height) {
                List<Integer> popped = stack.pop();
                width += popped.get(1);
                maxArea = Math.max(maxArea, popped.get(0) * width);
            }

            stack.push(List.of(height, width + 1));
            maxArea = Math.max(maxArea, height * (width + 1));
        }

        int w = stack.pop().get(1);

        while (!stack.empty()) {
            List<Integer> z = stack.pop();
            w += z.get(1);
            maxArea = Math.max(maxArea, z.get(0) * w);
        }

        return maxArea;
    }
}
