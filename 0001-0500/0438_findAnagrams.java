class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> startIndices = new ArrayList<>();

        if (s.length() < p.length()) return startIndices;

        Map<Character, Integer> window = new HashMap<>();

        for (int i=0; i < p.length(); i++) {
            char d = p.charAt(i);
            window.put(d, window.getOrDefault(d, 0) + 1);
        }

        for (int i=0; i < p.length(); i++) {
            char c = s.charAt(i);
            window.put(c, window.getOrDefault(c, 0) - 1);
            if (window.get(c) == 0) window.remove(c);
        }

        if (window.isEmpty()) startIndices.add(0);

        for (int i=p.length(); i<s.length(); i++) {
            char c = s.charAt(i);
            window.put(c, window.getOrDefault(c, 0) - 1);
            if (window.get(c) == 0) window.remove(c);
            
            char f = s.charAt(i - p.length());
            window.put(f, window.getOrDefault(f, 0) + 1);
            if (window.get(f) == 0) window.remove(f);

            if (window.isEmpty()) startIndices.add(i - p.length() + 1);
        }

        return startIndices;
    }
}
