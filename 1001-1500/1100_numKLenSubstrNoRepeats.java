class Solution {
    public int numKLenSubstrNoRepeats(String s, int k) {
        if (s.length() < k) return 0;
        HashMap<Character, Integer> window = new HashMap<>();
        int count = 0;
        for (int i=0; i<k; i++) window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);
        if (window.size() == k) count++;
        for (int i=k; i<s.length(); i++) {
            window.put(s.charAt(i-k), window.get(s.charAt(i-k)) - 1);
            if (window.get(s.charAt(i-k)) == 0) window.remove(s.charAt(i-k));
            window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);
            if (window.size() == k) count++;
        }
        return count;
    }
}
