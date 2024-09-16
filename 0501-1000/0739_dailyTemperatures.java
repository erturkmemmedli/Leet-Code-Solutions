class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<List<Integer>> stack = new Stack<>();
        int[] result = new int[n];
        int count;

        for (int i=n-1; i>=0; i--) {
            count = 1;
            while (!stack.empty() && stack.peek().get(0)<=temperatures[i]) {
                List<Integer> popped = stack.pop();
                count += popped.get(1);
            }

            if (stack.empty()) {
                result[i] = 0;
            } else {
                result[i] = count;
            }
            
            stack.push(List.of(temperatures[i], count));
        }

        return result;
    }
}
