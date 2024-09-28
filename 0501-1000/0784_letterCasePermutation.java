class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> output = new ArrayList<>();
        dp(output, s, 0, "");
        return output;
    }

    public void dp(List<String> output, String s, int index, String path) {
        if (index == s.length()) {
            output.add(path);
            return;
        }

        char c = s.charAt(index);
        
        if (c >= 48 && c <= 57) {
            dp(output, s, index + 1, path + c);
        } else {
            dp(output, s, index + 1, path + Character.toLowerCase(c));
            dp(output, s, index + 1, path + Character.toUpperCase(c));
        }
    }
}
