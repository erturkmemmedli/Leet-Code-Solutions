class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> output = new ArrayList<>();
        backtrack(s, output, new ArrayList<>());
        return output;
    }

    public void backtrack(String s, List<List<String>> output, List<String> path) {
        if (s.length() == 0) {
            output.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < s.length(); i++) {
            String str = s.substring(0, i + 1);
            if (isPalindrome(str)) {
                path.add(str);
                backtrack(s.substring(i + 1), output, path);
                path.remove(path.size() - 1);
            }
        }
    }

    public boolean isPalindrome(String s) {
        for (int i = 0; i < s.length()/2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
