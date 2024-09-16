class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        HashMap<Character, Integer> window = new HashMap<>();
        int minimum = Integer.MAX_VALUE;
        int counter = 0;
        int start = 0;
        int startIndex = 0;
        int endIndex = -1;

        for (int i = 0; i < t.length(); i++) {
            window.put(t.charAt(i), window.getOrDefault(t.charAt(i), 0) + 1);
        }

        for (int end = start; end < s.length(); end++) {
            if (window.containsKey(s.charAt(end))) {
                window.put(s.charAt(end), window.get(s.charAt(end)) - 1);
                if (window.get(s.charAt(end)) == 0) {
                    counter++;
                }
            }

            while (counter == window.size()) {
                if (minimum > end - start + 1) {
                    minimum = end - start + 1;
                    startIndex = start;
                    endIndex = end;
                }
                if (window.containsKey(s.charAt(start))) {
                    window.put(s.charAt(start), window.get(s.charAt(start)) + 1);
                    if (window.get(s.charAt(start)) > 0) {
                        counter--;
                    }
                }
                start++;
            }
        }

        return s.substring(startIndex, endIndex + 1);
    }
}
