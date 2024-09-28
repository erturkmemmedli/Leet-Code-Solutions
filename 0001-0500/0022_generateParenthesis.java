class Solution {
    public List<String> generateParenthesis(int n) {
        if (n == 0) {
            List<String> base = new ArrayList<>();
            base.add("");
            return base;
        }

        List<String> output = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (String left: generateParenthesis(i)) {
                for (String right: generateParenthesis(n - i - 1)) {
                    output.add("(" + left + ")" + right);
                }
            }
        }

        return output;
    }
}
