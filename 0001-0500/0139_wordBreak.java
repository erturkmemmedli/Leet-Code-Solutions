class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> set = new HashSet<>(wordDict);
        HashMap<Integer, Boolean> memo = new HashMap<>();
        return dp(set, memo, s, 0);
    }

    public boolean dp(HashSet<String> set, HashMap<Integer, Boolean> memo, String str, int idx) {
        if (idx == str.length()) {
            return true;
        }

        if (memo.containsKey(idx)) {
            return memo.get(idx);
        }

        boolean result = false;

        for (String s: set) {
            int l = s.length();
            if (idx+l <= str.length() && s.equals(str.substring(idx, idx+l))) {
                result = result || dp(set, memo, str, idx+l);
            }
        }

        memo.put(idx, result);
        return result;
    }
}
