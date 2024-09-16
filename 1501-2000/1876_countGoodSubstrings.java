class Solution {
    public int countGoodSubstrings(String s) {
        if (s.length() < 3) return 0;

        HashMap<Character, Integer> window = new HashMap<>();
        int count = 0;

        for (int i=0; i<3; i++) {
            window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);
        }

        if (window.size() == 3) count++;

        for (int i=3; i<s.length(); i++) {
            window.put(s.charAt(i-3), window.get(s.charAt(i-3)) - 1);

            if (window.get(s.charAt(i-3)) == 0) {
                window.remove(s.charAt(i-3));
            }

            window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);
            
            if (window.size() == 3) count++;
        }
        
        return count;
    }
}
