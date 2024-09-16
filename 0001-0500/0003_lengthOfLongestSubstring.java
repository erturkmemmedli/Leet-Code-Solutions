class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> window = new HashSet<>();
        int start = 0;
        int end = 0;
        int longest = 0;

        while (end < s.length()) {
            char c = s.charAt(end);

            while (window.size() > 0 && window.contains(c)) {
                window.remove(s.charAt(start));
                start++;
            }

            window.add(c);
            longest = Math.max(longest, window.size());
            end++;
        }

        return longest;
    }
}
