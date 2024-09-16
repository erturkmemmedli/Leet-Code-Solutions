class Solution {
    public int maximalRectangle(char[][] matrix) {
        int n = matrix[0].length;
        int[] heights = new int[n];
        int maxArea = 0;

        for (char[] h: matrix) {
            for (int i = 0; i < n; i++) {
                if (h[i] == '0') {
                    heights[i] = 0;
                } else {
                    heights[i] += (int) (h[i] - '0');
                }
            }
            
            maxArea = Math.max(maxArea, findLargestRectangle(heights));
        }

        return maxArea;
    }

    public int findLargestRectangle(int[] heights) {
        Stack<List<Integer>> stack = new Stack<>();
        int n = heights.length;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int height = heights[i];
            int width = 0;

            while (!stack.empty() && stack.peek().get(0) >= height) {
                List<Integer> popped = stack.pop();
                width += popped.get(1);;
                maxArea = Math.max(maxArea, popped.get(0) * width);
            }

            stack.push(List.of(height, width + 1));
            maxArea = Math.max(maxArea, height * (width + 1));
        }

        int w = 0;

        while (!stack.empty()) {
            List<Integer> temp = stack.pop();
            w += temp.get(1);
            maxArea = Math.max(maxArea, temp.get(0) * w);
        }

        return maxArea;
    }
}
